import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.allocationDB

allocation_history = database.get_collection("allocation_history")

async def create_indexes():
    # Creating an index on vehicle_id and allocation_date to searching faster
    await allocation_history.create_index([("vehicle_id", 1), ("allocation_date", 1)], name="vehicle_allocation_index")

def allocationDB_helper(allocationDB) -> dict:
    return {
        "allocation_id": str(allocation_history["_id"]),
        "employee_id": allocation_history["employee_id"],
        "employee_name": allocation_history["employee_name"],
        "vehicle_id": allocation_history["vehicle_id"],
        "allocation_date": allocation_history["allocation_date"].strftime("%Y-%m-%d")
    }