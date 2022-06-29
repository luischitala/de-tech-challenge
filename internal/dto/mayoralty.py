
# Pydantic
from pydantic import (
    BaseModel, Field
)

class Mayoralty(BaseModel):

    id:int = Field(alias="id")
    nomgeo:str = Field(alias="nomgeo")
    cve_mun:int 
    cve_ent:int
    cvegeo:int
    # Geometry field 
    geo_point_2d:str
    municipio:int

    # Extra configuration
    class Config():
        # Allow to use ORM mode
        orm_mode = True,
        # Example code for the response
        schema_extra = {
            "example": {
                    "id": 9,
                    "nomgeo": "Iztacalco",
                    "cve_mun": 6,
                    "cve_ent": 9,
                    "cvegeo": 9006,
                    "geo_point_2d": "19.396911897,-99.094329797",
                    "municipio": 6
            }
        }