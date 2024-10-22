from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from src.crud.allocation import retrieve_allocations, create_allocation
from src.models.allocation_history import AllocationSchema, ResponseModel
from src.database import allocation_history
from datetime import date, datetime


router = APIRouter(prefix="/allocation",
    tags=["Vehicle Allocation System"])


#api endpoint to vide all allocations
@router.get("/", response_description="Allocation history received")
async def get_allocations():
    allocations = await retrieve_allocations()
    if allocations:
        return ResponseModel(allocations, "Allocations data retrieved successfully")
    return ResponseModel(students, "Empty list returned")


#api endpoint to add new allocation
@router.post("/", response_description="Create a new allocation")
async def add_allocation(allocation: AllocationSchema = Body(...)):

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

    new_allocation = await create_allocation(allocation)
    return ResponseModel(new_allocation, "Allocation done successfully.")






