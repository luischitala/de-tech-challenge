from fastapi import APIRouter
from internal.infrastructure.router.v1.router import api_router as v1_router

# Generate an instance of API router to encapsulate the first version of this code to handle as modular logic
api_router = APIRouter()
# Include the actual router that will contain all the endpoints for this tech challenge
api_router.include_router(v1_router, prefix='/v1')