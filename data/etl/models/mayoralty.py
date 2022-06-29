# Base Imports
import json
# GeoORM and ORM imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape
from shapely.geometry import shape

#Retrieve the base model to generate the entities
Base = declarative_base()

#Declare the model Mayoralty
class Mayoralty(Base):
    __tablename__ = 'mayoralties'
    
    id = Column(Integer, primary_key=True)
    nomgeo = Column(String)
    cve_mun = Column(Integer)
    cve_ent = Column(Integer)
    cvegeo = Column(Integer)
    geo_point_2d = Column(String)
    geo_shape = Column(Geometry("POLYGON", srid=4326, spatial_index=True))
    municipio = Column(Integer)
    
    def __init__(self,row):
        geom_json = json.loads(row[7])
        valid_geom = shape(geom_json)
        self.id = row[0]
        self.nomgeo = row[2]
        self.cve_mun = row[3]
        self.cve_ent = row[4]
        self.cvegeo = row[5]
        self.geo_point_2d = row[6]
        self.geo_shape = from_shape(valid_geom)
        self.municipio = row[8]
