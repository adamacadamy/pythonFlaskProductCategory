# app/__init__.py
import os
from flask import Flask
from flask_restx import Api, Namespace, Resource
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    
    app.config["SQLALCHEMY_DATABASE_URI"]= os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    
    # Initialize extensions
    from app.models import db
    db.init_app(app)
    
    from app.schemas import api 
    api.init_app(app)
    
    from app.routes import register_routes 
    register_routes(api)
    
    return app