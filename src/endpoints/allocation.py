from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from src.crud.allocation import *
from src.models.allocation import AllocationSchema, ResponseModel
from src.database import allocation_history
from datetime import date, datetime
from bson.objectid import ObjectId



router = APIRouter(prefix="/allocation",
    tags=["Vehicle Allocation System"])



#api endpoint to create new allocation
@router.post("/", response_description="Create a new allocation")
async def create_allocation(allocation: AllocationSchema = Body(...)):

     # Convert allocation_date (date object) to a datetime object(mongo supported)
    #allocation_datetime = datetime.combine(allocation.allocation_date, datetime.min.time())
    
    # Check if the vehicle is already allocated for the given date
    existing_allocation = await allocation_history.find_one({
        "vehicle_id": allocation.vehicle_id,
        "allocation_date": allocation.allocation_date
    })
    
    allocation = jsonable_encoder(allocation)

    if existing_allocation:
        return ResponseModel(allocation, "Vehicle is already allocated for this date.")

    new_allocation = await add_allocation(allocation)
    return ResponseModel(new_allocation, "Allocation done successfully.")


#api endpoint to view all allocations
@router.get("/", response_description="Allocation history received")
async def get_allocations():
    allocations = await retrieve_allocations()
    if allocations:
        return ResponseModel(allocations, "Allocations data retrieved successfully")
    return ResponseModel(students, "Empty list returned")

    
#api to delete an allocation
@router.delete("/{allocation_id}", response_description="Allocation data deleted from the database")
async def delete_allocation_data(allocation_id: str):
    deleted_allocation = await delete_allocation(allocation_id)
    if deleted_allocation:
        return ResponseModel(
            "Allocation with ID: {} removed".format(allocation_id), "Successfully Deleted"
        )
    return ResponseModel(
        "An error occurred", "Allocation with id {} doesn't exist".format(allocation_id)
    )











