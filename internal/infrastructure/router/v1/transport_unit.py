# Python
import sys
sys.path.append("..")
from typing import (List,Optional)
# FastAPI
from fastapi import (
    APIRouter, status, Depends, Query
)
# Entities and Dto dependencies
from internal.dto.transport_unit import TransportUnit as unit_dto
from internal.entity.transport_unit import TransportUnit as unit_entity
# ORM dependencies
from sqlalchemy.orm import Session
# Database dependency to inject into the controllers
from internal.infrastructure.database.db import get_db
# Controller
from internal.controller.v1.handlers.transport_unit import TransportUnitController
# Main API router instance generation
router = APIRouter()

# Values and documentation for the swagger endpoint
@router.get(
            path='/',
            status_code=status.HTTP_200_OK,
            response_model=List[unit_dto],
            summary='Muestra las unidades de metrobús disponibles',
            tags=['Metrobuses'])

# Endpoint that calls the method get_units 
def get_transport_units(db: Session = Depends(get_db)):
    """
    Este endpoint muestra todas las unidades del metrobús disponibles

    Regresa un objeto json con el resultado.
    """
    # Call the controller method to retrieve the response
    response =  TransportUnitController(db).get_units()
    # Handle the empty response
    if response == None:
        response = []

    return response

# Values and documentation for the swagger endpoint
@router.get(
            path="/{id}",
            status_code=status.HTTP_200_OK,
            response_model=unit_dto,
            summary='Muestra la unidad de metrobús por su id',
            tags=['Metrobuses'])
 
# Endpoint that calls the method get_unit_by_id and receives an id as a parameter
def get_transport_unit(id: int, db: Session = Depends(get_db)):
    """

    Este endpoint muestra una unidad del metrobús basado en su id

    Parameters:
    - (Required) id

    Regresa un objeto json con el resultado.

    """
    # Call the controller method to retrieve the response
    response =  TransportUnitController(db).get_unit_by_id(id)
    # Handle the empty response 
    if response == None:
        response = []

    return response

# Values and documentation for the swagger endpoint
@router.get(
    path='/alcaldia/{mayoralty}',
    response_model=List[unit_dto],
    status_code=status.HTTP_200_OK,
    summary='Muestra las unidades del metrobús que estén dentro de una alcaldía',
    tags=['Metrobuses']
    )

# Endpoint that calls the method get_unit_by_mayoralty and receives a mayoralty as a parameter
def get_unit_by_mayoralty(mayoralty: Optional[str] = Query(
        default=["Tlalpan", "Cuauhtmoc"],
        title="Alcaldía",
        description="Alcaldía dendro de la cual se van a buscar unidades disponibles",
        example="Tlalpan"
        ),db: Session = Depends(get_db)):

    """
    Este endpoint muestra las unidades del metrobús disponibles por alcaldía

    Parameters:
    - (Required) alcaldia

    Regresa un objeto json con el resultado.
    """
    # Call the controller method to retrieve the response
    response_list =  TransportUnitController(db).get_unit_by_mayoralty(mayoralty)
    # Handle the empty response
    if response_list == None:
        response_list = []

    return response_list
