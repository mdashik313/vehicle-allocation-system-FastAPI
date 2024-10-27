from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional
from bson.objectid import ObjectId



class AllocationSchema(BaseModel):  #model to mapping the database
    employee_id: int = Field(..., gt=0, lt=1001)
    employee_name: str = Field(...)
    vehicle_id: int = Field(..., gt=0, lt=1001)
    allocation_date: str = Field(...)

    @validator("allocation_date")
    def check_allocation_date(cls, value):
        
        allocation_date_obj = datetime.strptime(value, "%Y-%m-%d").date() # Convert the string to a date object

        if allocation_date_obj < date.today():  # Compare the allocation date with today's date
            raise ValueError("Allocation date must be greater than or equal to today's date.")
        
        # If validation passes, return the original value
        return value

    class Config:  #JSON example that will display in API documentation
        json_schema_extra = { 
            "example": {
                "employee_id": 1,
                "employee_name": "Ashik",
                "vehicle_id": 1,
                "allocation_date": "2024-10-22"
            }
        }


class UpdateAllocation(BaseModel):  #model for updating allocation
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
        
        allocation_date_obj = datetime.strptime(value, "%Y-%m-%d").date() # Convert the string to a date object

        if allocation_date_obj <= date.today():  # Check whether the allocation date is set for futere
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


class SearchFilterSchema(BaseModel):   #model for search/filter
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


def ResponseModel(data, message):  #custom response model
    return {
        "data": [data],
        "message": message,
    }


