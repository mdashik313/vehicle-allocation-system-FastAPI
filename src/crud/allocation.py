from src.database import allocation_history, allocationDB_helper

#crud operations

async def retrieve_allocations():
    allocations = []
    async for allocation in allocation_history.find():
        allocations.append(allocationDB_helper(allocation))
    return allocations



