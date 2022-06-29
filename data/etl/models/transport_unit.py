# ORM and GeoORM dependencies
from sqlalchemy import Column, Integer, String, Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from geoalchemy2.shape import  from_shape
from shapely.geometry import Point
#Retrieve the base model to generate the entities
Base = declarative_base()

#Declare the model Transport Unit
class TransportUnit(Base):
    __tablename__ = 'transport_units'
    
    id = Column(Integer, primary_key = True)
    date_updated = Column(DateTime)
    vehicle_id = Column(Integer)
    vehicle_label = Column(Integer)
    vehicle_current_status = Column(Integer)
    position_latitude = Column(Float)
    position_longitude = Column(Float)
    geographic_point = Column(Geometry("POINT", srid = 4326, spatial_index = True))
    position_speed = Column(Integer)
    position_odometer = Column(Integer)
    trip_schedule_relationship = Column(Integer)
    trip_id = Column(Integer, nullable = True)
    trip_start_date = Column(Integer, nullable = True)
    trip_route_id = Column(Integer, nullable = True)
    mayoralty = Column(String, nullable = True)
    
    def __init__(self,row):
        self.id = row[0]
        self.date_updated = row[2]
        self.vehicle_id = row[3]
        self.vehicle_label = row[4]
        self.vehicle_current_status = row[5]
        self.position_latitude = float(row[6])
        self.position_longitude = float(row[7])
        self.geographic_point = from_shape(Point(self.position_longitude, self.position_latitude), srid=4326)
        self.position_speed = row[9]
        self.position_odometer = row[10]
        self.trip_schedule_relationship = row[11]
        self.trip_id = row[12] 
        self.trip_start_date = row[13]
        self.trip_route_id = row[14]
