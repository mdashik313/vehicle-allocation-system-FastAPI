from fastapi import APIRouter
from src.endpoints import allocation

router = APIRouter()
router.include_router(allocation.router)

