# Import the main APIRouter
from fastapi import APIRouter
# Import the routers from infrastructure layer to separate logic
from internal.infrastructure.router.v1.mayoralty import router as mayoralty_router
from internal.infrastructure.router.v1.transport_unit import router as transport_router

api_router = APIRouter()
# Map and include the actual routers from the infrastructure layer
api_router.include_router(mayoralty_router, prefix='/alcaldias')
api_router.include_router(transport_router, prefix='/metrobuses')