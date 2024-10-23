from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional
from bson.objectid import ObjectId



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

    @validator("allocation_id")
    def validate_object_id(cls, value):
        # Validate that allocation_id is a valid ObjectId
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid allocation ID format. Must be a 24-character hex string.")
        return value

    @validator("allocation_date")
    def check_allocation_date(cls, value):
        # Convert the string to a date object
        allocation_date_obj = datetime.strptime(value, "%Y-%m-%d").date()

        # Check whether the allocation date is set for futere
        if allocation_date_obj <= date.today():
            raise ValueError("Can not update, because allocation date is passed..")
        
        # If validation passes, return the original value
        return value
    
    

    class Config:
        json_schema_extra = {
            "example": {
                "allocation_id": "yourAllocationID",
                "vehicle_id": 1,
                "allocation_date": "2024-10-22"
            }
        }



class FilterByAllocationID(BaseModel):
    allocation_id: Optional[str] = Field(None)

    @validator("allocation_id")
    def validate_object_id(cls, value):
        # Validate that allocation_id is a valid ObjectId
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid allocation ID format. Must be a 24-character hex string.")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "allocation_id": "yourAllocationID"
            }
        }

class SearchFilterSchema(BaseModel):
    allocation_id: Optional[str]
    employee_id: Optional[int] 
    vehicle_id: Optional[int] 
    allocation_date: Optional[str] 

    class Config:
        json_schema_extra = {
            "example": {
                "allocation_id": "yourAllocationID",
                "employee_id": 1,
                "vehicle_id": 1,
                "allocation_date": "2024-10-22"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "message": message,
    }


