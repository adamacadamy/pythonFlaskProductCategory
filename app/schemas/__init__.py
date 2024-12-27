import os
from flask_restx import Api
  
app_title = os.getenv("APP_TITLE", "product and Category Management API")
app_version= os.getenv("APP_VERSION","1.0" )
app_description = os.getenv("APP_DESCRIPTION","API for managing products and categories.")

api = Api(
    title=app_title,
    version=app_version,
    description=app_description
)