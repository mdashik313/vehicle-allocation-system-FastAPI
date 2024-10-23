import uvicorn
from fastapi import FastAPI
from src.database import create_indexes
from routes.api import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        await create_indexes()  # creates indexes on the collections
        print("Database configured and indexes created successfully.")
    except Exception as e:
        print(f"Error during startup: {e}")


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    