import os
import environ 
from typing import Any, Dict, List
from pydantic import AnyHttpUrl

# Variables
DEBUG = True
PORT = 8000
API: str = '/api'
PROJECT_NAME: str = 'Sefira Tech challenge'
DESCRIPTION: str = 'FastAPI Implementation for the transport units and mayoralties API'
VERSION: str = '1.0.0'
DOCS: str = '/docs'
SWAGGER_UI_PARAMETERS: Dict[str, Any] = {
         'displayRequestDuration': True,
     'filter': True,
}
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

