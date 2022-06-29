# Import the the entities and dtos
from internal.dto.transport_unit import TransportUnit as unit_dto
from internal.entity.transport_unit import TransportUnit as unit_entity
# Typing, app and orm libraries
from typing import List
from sqlalchemy.orm import Session
from fastapi  import HTTPException 

# Main transport unit controller
class TransportUnitController():

    # Constructor method that will take the db session as an injected dependency 
    def __init__(self, db: Session):
        self.db = db

    # Method that will handle the business logic for the api_v1_metrobuses_alcaldia endpoint and return a valid response to the router
    def get_units(self)-> List[unit_dto]:
        # Get the transport units
        response = self.db.query(unit_entity).all()
        # Handle empty Queryset
        if response == []:
            raise HTTPException(status_code=404, detail="No items found")
        json_response = {}
        return response

    # Method that will handle the business logic for the api_v1_metrobuses_alcaldia endpoint and return a valid response to the router
    def get_unit_by_mayoralty(self, mayoralty:None )-> List[unit_dto]:
        # Get the transport unit by using its mayoralty
        response = self.db.query(unit_entity).filter(unit_entity.mayoralty==mayoralty).all()
        # Handle empty Queryset
        if response == []:
            raise HTTPException(status_code=404, detail="Item not found")
        json_response = {}
        return response

    # Method that will handle the business logic for the api_v1_metrobuses_alcaldia_id endpoint and return a valid response to the router
    def get_unit_by_id(self, id:None )-> unit_dto:
        # Get the transport unit by using its id
        response = self.db.query(unit_entity).filter(unit_entity.id==id).first()
        # Handle empty Queryset
        if response == []:
            raise HTTPException(status_code=404, detail="Item not found")
        json_response = {}

        return response




