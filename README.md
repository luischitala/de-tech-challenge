
  

  

# DATA ENGINEER TECH CHALLENGE

  

  

  

##  Table of Contents:

  

  

- [Introduction](#introduction)

  

  

- [Table of Contents:](#table-of-contents)

  

  

- [Description](#description)

  

  

- [Software Architecture](#software-architecture)

  

  

- [Solution Diagram](#solution-diagram)

  

  

- [ETL](#etl)

  

  

- [DDL](#ddl)

  

  

- [Entities](#entities)

  

  

- [Features](#features)

  

  

- [Endpoints](#endpoints)

  

  

- [México's Open Data API](#mexicos-open-data-api)

  

  

- [Requirements:](#requirements)

  

  

- [Relevant Dependencies:](#relevant-dependencies)

- [Deployment Details](#deployment-details)

  

- [Installation](#installation)

  

  

- [With docker](#with-docker)

  

  

- [Basic Usage](#basic-usage)

  

  

- [Unit Testing](#unit-testing)

  

  

##  Description

  

  

This project is a simple REST API made with FastAPI as a requirement for the data engineer tech challenge.

  

  

It basically consults an external API by using an ETL, that transforms the response data to populate a database which allows geometry data types

  

  

##  México's Open Data API

  

  

  

Project that belongs to the Government of México, which serve many different data by sharing it with APIs and datasets, along with other tools like real time data streaming and data visualizations among other tools.

  

  

  

Link:

  

  

https://datos.gob.mx/

  

  

The sections that will be consulted by this project will be:

  

  

- [https://datos.cdmx.gob.mx/dataset/prueba_fetchdata_metrobus/resource/ad360a0e-b42f-482c-af12-1fd72140032e?inner_span=True](https://datos.cdmx.gob.mx/dataset/prueba_fetchdata_metrobus/resource/ad360a0e-b42f-482c-af12-1fd72140032e?inner_span=True)

  

- https://datos.cdmx.gob.mx/dataset/alcaldias

  

  

  

###  Software Architecture

  

  

It has been created following the Clean Architecture Principles to disengage the logic between layers.

  

  

The FastAPI core structure allows to easy implement [Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/) one of many reasons why this Framework has been choosed.

  

  

![clean architecture pattern](https://miro.medium.com/max/1400/1*D1EvAeK74Gry46JMZM4oOQ.png)

  

[Credits](https://medium.com/android-news/thoughts-on-clean-architecture-b8449d9d02df)

  

  

###  Solution Diagram

  

  

The solution for this challenge has been completed using micro services with docker, as it is shown in the diagram below.

  

  

The database definition has been made in the database creation domain, instead of the migration technique (using Alembic) due to Incompatibility issues.

  

  

![Solution Diagram](https://github.com/luischitala/de-tech-challenge/blob/master/docs/uml_diagram.PNG?raw=true)

  

###  Database

  

  

The database selected for this project was PostgreSQL along with the PostGIS extension, which allows us to store geometrical data, and also to do spatial queries which made this project's solution optimal.

  

  

The image implemented was Kartoza/postgis which can be downloaded in the following [Link](https://hub.docker.com/r/kartoza/postgis/)

  

  

![Database](https://zonegis.es/wp-content/uploads/2017/03/PostgrePostGIS.png)

  

[Credits](https://zonegis.es/guia-de-instalacion-de-postgresql-y-postgis/)

  

  

###  Entities

  

  

The entities for this project are:

  

  

- Mayoralty (Alcaldía)

  

- Transport Unit (Unidad del metrobús)

  

  

Both entities have two representations, the first is the Model, which is made by using SQLAlchemy and allows to the database layer to interact with data, and the second is the Schema (DTO) form using Pydantic, which allows to query the data.

  

  

###  DDL

  

  

The data model design will be composed of the two main entities tables, along with the required tables by PostGIS to work properly.

  

  

![DDL](https://github.com/luischitala/de-tech-challenge/blob/master/docs/ddl_tables.PNG?raw=true)

  

  

###  ETL

  

  

The ETL process, is composed of a python script, which uses the SQLAlchemy ORM to define the models that have been mapped, using as reference the response object from the Mexico's Open Data Project.

  

  

The ETL service, waits a certain amount of time, until the database service starts and it runs the initial script which creates the tables: mayoralties & transport_units.

  

  

Once the connection between the ETL script and the database has been successfully made, it starts to send http requests to the Mexico's Open Data API, firstly to retrieve the mayoralties because they will be the base to allow the second requests perform a Geographical Query, using the area from mayoralties to discover to which mayoralty each transport unit belongs to.

  

  

When both requests have been completed, the FastAPI Service will be ready ready to serve the data by using different endpoints.

There's also a DAG format ETL valid format to execute with Apache Airflow, and a Jupyter notebook where all the data discovery was made.

The ETL was separated in different functions to make the code scalable. 
  

  

###  Features

  

  

Features included:

  

  

- Docker, Compose Environment

  

  

- Data modeling with Pydantic and SQLAlchemy

  

  

- FastAPI Application

  

  

- Swagger Documentation

  

  

- External API connection

  

  

###  Endpoints

  

  

Base URL:

  

  

http://127.0.0.1:8080/api/v1

  

  

- /alcaldias -Returns all mayoralties

  

- /metrobuses -Returns all transport units

  

- /metrobuses/{id} -Return a transport unit by ID

  

- /metrobuses/alcaldia/{mayoralty} -Return a list of transport units by mayoralties

  

  

  

###  Requirements:

  

  

- Docker

  

  

  

###  Relevant Dependencies:

  

  

- FastAPI == 0.75.2

  

  

- Psycopg == 2.8.6

  

  

- Uvicorn == 0.17.6

  

  

- Django Environ == 0.8.1

  

  

- Httpx == 0.22.0

  

  

- SQLAlchemy == 1.4

  

  

- Pydantic == 1.9.0

  

###  Deployment details

  

The main docker-compose file is located in the folder /deployments/, and all the service Dockerfiles are located in that directory, along with their K8s manifest files.

  

###  Installation

  

1. Clone or download de repository:

  
  

```

  

$ git clone https://github.com/luischitala/de-tech-challenge

  

```

  

  

  

###  With docker

  

  

1. Run it with Docker Compose.

  

  

```bash

  

$ cd de-tech-challenge/de-tech-challenge

  

$ docker-compose -f ./deployment/docker-compose.yml build

swa

$ docker-compose -f ./deployment/docker-compose.yml up -d

  

```

  

  

###  Basic Usage

  

  

Once you are running the server open the [Swagger UI App](http://localhost:8080/docs) to checkout the API documentation.

  

  

The example is shown in the picture bellow.

  

![Swagger](https://github.com/luischitala/de-tech-challenge/blob/master/docs/swagger.PNG?raw=true)

  

  

###  Unit Testing

  

Once the project has been built and the containers started.

  

Run the following command at the root of the project.

  

```bash

$ docker exec -it deployment-app-1 python -m pytest

```
