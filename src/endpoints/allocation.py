from fastapi import APIRouter, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from src.crud.allocation import *
from src.models.allocation import *
from src.database import allocation_history
from datetime import date, datetime
from bson.objectid import ObjectId



router = APIRouter(prefix="/allocation",
    tags=["Vehicle Allocation System"])



#api endpoint to create new allocation
@router.post("/", response_description="Create a new allocation")
async def create_allocation(allocation: AllocationSchema = Body(...)):  

    
    # Check if the vehicle is already allocated for the given date
    existing_allocation = await allocation_history.find_one({
        "vehicle_id": allocation.vehicle_id,
        "allocation_date": allocation.allocation_date
    })
    
    allocation = jsonable_encoder(allocation)   #converting pydentic models to JSON Compatible datatype

    if existing_allocation:
        return ResponseModel(allocation, "Vehicle is already allocated for this date.")

    new_allocation = await add_allocation(allocation)
    return ResponseModel(new_allocation, "Allocation done successfully.")


#api endpoint to view all allocations
@router.get("/", response_description="Allocation history received")
async def view_all_allocations():
    allocations = await retrieve_allocations()
    if allocations:
        return ResponseModel(allocations, "Allocations data retrieved successfully")
    return ResponseModel(allocations, "Empty list returned")



#api to delete an allocation
@router.delete("/{allocation_id}", response_description="Allocation data deleted from the database.")
async def delete_allocation(allocation_id: str):
    # Cehcking that the allocation_id is a valid ObjectId
    if not ObjectId.is_valid(allocation_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid allocation ID format. Must be a 24-character hex string."
        )

    deleted_allocation = await delete_allocation_data(allocation_id)

    if deleted_allocation == 1:
        return ResponseModel(
            "Allocation with ID: {} removed".format(allocation_id), "Successfully Deleted"
        )
    elif deleted_allocation == 0:
        return ResponseModel(
            "Deleting can't be processed", "Date is not a future date."
        )
    elif deleted_allocation == 2:
        return ResponseModel(
                "An error occured", "Allocation with id {} doesn't exist".format(allocation_id)
            )

#api to update an allocation
@router.put("/", response_description="Allocation data updated.")
async def update_allocation(allocation : UpdateAllocation = Body(...)):
    allocation = jsonable_encoder(allocation)
    updated_allocation, message = await update_allocation_data(allocation)
    return ResponseModel(updated_allocation,message)
    

#api for filtering allocations
@router.post("/search", response_description="Search allocations")
async def history_report_filter(search_params: SearchFilterSchema = Body(...)):

    search_params = {k: v for k, v in search_params.dict().items() if v is not None}   #taking only those attributes that is not null

    result = await filter_allocation(search_params)

    if result:
        return ResponseModel(result, "Result(s) found.")
    
    return ResponseModel(result, "No result found.")








