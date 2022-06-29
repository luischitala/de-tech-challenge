# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel,  Field
)

class TransportUnit(BaseModel):
    id: str = Field(alias="id")
    date_updated:date
    vehicle_id:int
    vehicle_label:int
    vehicle_current_status:int
    position_latitude:float
    position_longitude:float
    # geographic_point = Column(Geometry("POINT", srid = 4326, spatial_index = True))
    position_speed:int
    position_odometer:int
    trip_schedule_relationship:int
    trip_id:Optional[int]=None
    trip_start_date:Optional[int]=None
    trip_route_id:Optional[int]=None
    mayoralty:Optional[str]=None

    class Config():
        orm_mode = True,
        schema_extra = {
            "example" : {
                "id": "2",
                "date_updated": "2021-01-27",
                "vehicle_id": 177,
                "vehicle_label": 119,
                "vehicle_current_status": 1,
                "position_latitude": 19.292600631713867,
                "position_longitude": -99.17749786376952,
                "position_speed": 13,
                "position_odometer": 0,
                "trip_schedule_relationship": 0,
                "trip_id": 9732304,
                "trip_start_date": 20200428,
                "trip_route_id": 367,
                "mayoralty": "Tlalpan"
            }
        }
