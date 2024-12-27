from flask_restx import fields
from app.schemas import api

""" 
READONLY MEANS = VALID ONLY FOR GET, PUT, DELETE  BUT NOT FOR POST
"""
category_model = api.model('Category', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the category'),
    'name': fields.String(required=True, description='Name of the category'),
    'description': fields.String(description='Description of the category')
})