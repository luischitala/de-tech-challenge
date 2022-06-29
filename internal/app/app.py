# Fast API dependencies
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from internal.config import settings
from internal.infrastructure.router.router import api_router
from internal.usecase.utils import http_exception_handler

# Function that define all the parameters to fully generate an instance of FastAPI main app
def create_app() -> FastAPI:
    # Consult the settings to get the private variables
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        openapi_url='{0}/openapi.json'.format(settings.DOCS),
        swagger_ui_parameters=settings.SWAGGER_UI_PARAMETERS,
    )
    # Configure the required middlewares and configurations
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                str(origin)
                for origin in settings.BACKEND_CORS_ORIGINS
            ],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )
    #Add the routers and extra configuration
    app.include_router(api_router, prefix=settings.API)
    app.add_exception_handler(HTTPException, http_exception_handler)

    return app