import motor.motor_asyncio


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.allocationDB
allocation_history = database.get_collection("allocation_history")


async def create_indexes():
    # Creating an index on vehicle_id and allocation_date to searching faster
    await allocation_history.create_index([("vehicle_id", 1), ("allocation_date", 1)], name="vehicle_allocation_index")

def allocationDB_helper(allocation) -> dict:
    return {
        "allocation_id": str(allocation["_id"]),
        "employee_id": allocation["employee_id"],
        "employee_name": allocation["employee_name"],
        "vehicle_id": allocation["vehicle_id"],
        "allocation_date": allocation["allocation_date"]
    }