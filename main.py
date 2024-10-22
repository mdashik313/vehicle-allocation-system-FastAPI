import uvicorn
from fastapi import FastAPI
from src.database import create_indexes

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await create_indexes() 

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    