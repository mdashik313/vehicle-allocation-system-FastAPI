from pydantic import BaseModel, Field, validator
from datetime import date, datetime

class AllocationSchema(BaseModel):
    employee_id: int = Field(..., gt=0, lt=1001)
    employee_name: str = Field(...)
    vehicle_id: int = Field(..., gt=0, lt=1001)
    allocation_date: str = Field(...)

    @validator("allocation_date")
    def check_allocation_date(cls, value):
        # Convert the string to a date object
        allocation_date_obj = datetime.strptime(value, "%Y-%m-%d").date()

        # Compare the allocation date with today's date
        if allocation_date_obj < date.today():
            raise ValueError("Allocation date must be greater than or equal to today's date.")
        
        # If validation passes, return the original value
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "employee_id": 1,
                "employee_name": "Ashik",
                "vehicle_id": 1,
                "allocation_date": "2024-10-22"
            }
        }


class UpdateAllocation(BaseModel):
    allocation_id: str = Field(...)
    vehicle_id: int = Field(..., gt=0, lt=1001)
    allocation_date: str = Field(...)

    @validator("allocation_date")
    def check_allocation_date(cls, value):
        # Convert the string to a date object
        allocation_date_obj = datetime.strptime(value, "%Y-%m-%d").date()

        # Check whether the allocation date is set for futere
        if allocation_date_obj > date.today():
            raise ValueError("Can not update, because allocation date is passed..")
        
        # If validation passes, return the original value
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "allocation_id": "yourAllocationId",
                "vehicle_id": 1,
                "allocation_date": "2024-10-22"
            }
        }



def ResponseModel(data, message):
    return {
        "data": [data],
        "message": message,
    }


