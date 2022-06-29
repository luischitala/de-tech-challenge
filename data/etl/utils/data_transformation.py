from models.mayoralty import Mayoralty
from models.transport_unit import TransportUnit

#ORM and GeoORM libraries
import shapely.wkt

# Auxiliar function that parses a response object to json object
def transform_to_json(response):
    #Parse the response to json format
    json_response = response.json()
    return json_response

# Auxiliar function to retrieve only the values from the dictionaries to simply the constructor input value
def transform_to_list(register):
    register_list = []
    register_values = register.values()
    register_list = list(register_values)
    return register_list

# Function that transforms a request list of records to an ORM objects and persist into a database
def process_normal_records(session, records):
    #Iterate the parsed response
    for record in records:
        #Apply the transformation function
        clean_record = transform_to_list(record)
        #Generate a new instance of the model
        mayoralty = Mayoralty(clean_record)
        exists = session.query(Mayoralty.id).filter_by(id=clean_record[0]).first() is not None
        if not exists:
            session.add(mayoralty)
        #Persist the iteration
    # Persist the data 
    session.commit()
    print('Records succesfully saved into the database')

# Function that transforms a request list of records to an ORM objects and persist into a database
def process_geom_records(session, records, geometry):

    for record in records:
        #Apply the transformation function
        clean_record = transform_to_list(record)
        #Generate a new instance of the model
        unit = TransportUnit(clean_record)
        exists = session.query(TransportUnit.id).filter_by(id=clean_record[0]).first() is not None
        if not exists:
            #Retrieve the point to query using the GeORM
            if geometry == 'POINT':
                point = unit.geographic_point
                #Verify if the point indicated on the geom column belongs to any mayoralty
                mayoralty = session.query(Mayoralty).filter(Mayoralty.geo_shape.ST_Contains(point)).first()
                #If ther's a matching mayoralty persist in to the transport unit column
                if mayoralty != None:
                    unit.mayoralty = mayoralty.nomgeo
                    session.add(unit)
    # Persist the data 
    session.commit()
    print('Records succesfully saved into the database')

    
