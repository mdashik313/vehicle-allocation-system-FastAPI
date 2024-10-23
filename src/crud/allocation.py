from src.database import allocation_history, allocationDB_helper
from bson.objectid import ObjectId


#crud operations

# Retrieve allocation history
async def retrieve_allocations():
    allocations = []
    async for allocation in allocation_history.find():
        allocations.append(allocationDB_helper(allocation))
    return allocations

# Create a new allocation to the database
async def add_allocation(allocation_data: dict) -> dict:
    allocation = await allocation_history.insert_one(allocation_data)
    new_allocation = await allocation_history.find_one({"_id": allocation.inserted_id})
    return allocationDB_helper(new_allocation)


#Delete an allocation
async def delete_allocation(id : str):
    allocation = await allocation_history.find_one({"_id": ObjectId(id)})
    if allocation:
        await allocation_history.delete_one({"_id": ObjectId(id)})
        return True

