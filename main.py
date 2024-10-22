import uvicorn
from fastapi import FastAPI
from src.database import db_config, create_indexes
from routes.api import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        db_config()  # setup mongoDB database
        await create_indexes()  # creates indexes on the collections
        print("Database configured and indexes created successfully.")
    except Exception as e:
        print(f"Error during startup: {e}")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    