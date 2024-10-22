from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.crud import retrieve_allocations, create_allocation
from src.models.allocation_history import AllocationSchema
from src.database import allocation_history

router = APIRouter(prefix="/allocation",
    tags=["Vehicle Allocation System"])


#api endpoint to add new allocation
@router.post("/", 
    response_description="Create a new allocation", 
    status_code=status.HTTP_201_CREATED, 
    response_model=AllocationSchema
)
async def add_allocation(allocation: AllocationSchema = Body(...)):
    
    # Check if the vehicle is already allocated for the given date
    existing_allocation = await allocation_history.find_one({
        "vehicle_id": allocation.vehicle_id,
        "date": allocation.allocation_date
    })
    
    if existing_allocation:
        return ResponseModel(allocation, "The vehicle is already allocated for that day")

    allocation = jsonable_encoder(allocation)
    new_allocation = await create_allocation(allocation)
    return ResponseModel(new_student, "Allocation done successfully.")






