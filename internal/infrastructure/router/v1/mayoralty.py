# Python
import sys
sys.path.append("..")
from typing import List
# FastAPI
from fastapi import (
    APIRouter, status, Depends
)

# Entity and Dto imports
from internal.dto.mayoralty import Mayoralty as mayoralty_dto
from internal.entity.mayoralty import Mayoralty as mayoralty_entity
# Database dependency
from internal.infrastructure.database.db import get_db
from sqlalchemy.orm import Session
from internal.controller.v1.handlers.mayoralty import MayoraltyController

# Routerdeclaration
router = APIRouter()
# /api/v1/alcaldias/ endpoint that will return a list of available mayoralties
@router.get(
            path='/',
            status_code=status.HTTP_200_OK,
            response_model=List[mayoralty_dto],
            summary='Lista de Alcaldías',
            tags=['Alcaldías'])

# Endpoint that calls the method get_units 
def get_mayoralties(db: Session = Depends(get_db)):
    """
    Este endpoint muestra todas las unidades del metrobus disponibles

    Regresa un objeto json con el resultado.
    """
    # Call the controller method to retrieve the response
    response =  MayoraltyController(db).get_mayoralties()
    # Handle the empty response
    if response == None:
        response = []

    return response