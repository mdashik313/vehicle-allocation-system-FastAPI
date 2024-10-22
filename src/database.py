import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.allocationDB

allocation_history = database.get_collection("allocation_history")


def allocationDB_helper(allocationDB) -> dict:
    return {
        "allocation_id": str(allocation_history["_id"]),
        "employee_id": allocation_history["employee_id"],
        "employee_name": allocation_history["employee_name"],
        "vehicle_id": allocation_history["vehicle_id"],
        "allocation_date": allocation_history["allocation_date"].strftime("%Y-%m-%d")
    }