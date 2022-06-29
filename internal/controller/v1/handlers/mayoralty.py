# Import the the entities and dtos
from internal.dto.mayoralty import Mayoralty as mayoralty_dto
from internal.entity.mayoralty import Mayoralty as mayoralty_entity
# Typing, app and orm libraries
from typing import List
from sqlalchemy.orm import Session
from fastapi  import HTTPException 

# Main transport unit controller
class MayoraltyController():

    # Constructor method that will take the db session as an injected dependency 
    def __init__(self, db: Session):
        self.db = db

    # Method that will handle the business logic for the api_v1_alcaldias endpoint and return a valid response to the router
    def get_mayoralties(self)-> List[mayoralty_dto]:
        # Get the available mayoralties
        response = self.db.query(mayoralty_entity).all()
        # Handle empty Queryset
        if response == []:
            raise HTTPException(status_code=404, detail="No items found")
        json_response = {}
        return response



