from flask_restx import fields 
from app.schemas import api
""" 
READONLY MEANS = VALID ONLY FOR GET, PUT, DELETE  BUT NOT FOR POST
"""

product_model = api.model('Product', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the product'),
    'name': fields.String(required=True, description='Name of the product'),
    'price': fields.Float(required=True, description='Price of the product'),
    'category': fields.String(attribute='category.name', description='Category of the product')
})