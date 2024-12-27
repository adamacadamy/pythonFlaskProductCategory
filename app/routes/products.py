from flask_restx import Namespace, Resource
from app.models.products import Product 
from app.models import db
from app.schemas.product_schema import product_model
 
product_ns = Namespace('products', description="Product operations")

@product_ns.route('/')
class ProductList(Resource):
    
    @product_ns.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return Product.query.all() # returns list of products 
       
    
    @product_ns.expect(product_model)
    def post(self):
        """Create a new product"""
        data = product_ns.payload
        new_product = Product(
                name=data['name'],
                price=data['price'],
                category_id=data['category']
            )
        db.session.add(new_product)
        db.session.commit()
        
        return new_product, 201

@product_ns.route('/<int: id>')
class ProductDetails(Resource):
    
    @product_ns.marshal_with(product_model)
    def get(self, id: int):
        """Retrieve a product by ID"""
        return Product.query.get_or_404(id)
    
    def delete(self, id: int):
        """Delete a product by ID"""
        product = Product.query.get_or_404(id) 
        db.session.delete(product)
        db.session.commit()
        
        return f"successfully deleted product with id {id}", 204