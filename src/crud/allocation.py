from src.database import allocation_history, allocationDB_helper
from bson.objectid import ObjectId
from datetime import date, datetime


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
        allocation_date_str = datetime.strptime(allocation["allocation_date"], "%Y-%m-%d").date()
        if allocation_date_str >= date.today():
            return 0  # let 0 means date it is not future date
        else: 
            await allocation_history.delete_one({"_id": ObjectId(id)})
            return 1  # let 1 means successfully deleted
    return 2  #let 2 means date doesn't exist


