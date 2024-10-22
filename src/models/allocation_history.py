from pydantic import BaseModel
from datetime import date

class AllocationSchema(BaseModel):
    employee_id: str = Field(..., gt=0, lt=1001)
    employee_name: str = Field(...)
    vehicle_id : str = Field(..., gt=0, lt=1001)
    allocation_date: date =  Field(..., ge=date.today())

    class Config:
        json_schema_extra = {
            "example": {
                "employee_id": "2",
                "employee_name": "Asif Ahmed",
                "vehicle_id": "5",
                "allocation_date": "2024-10-22"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

