from flask_restx import Namespace, Resource
from app.models.categories import Category
from app.models import db
from app.schemas.category_schema import category_model
 
category_ns = Namespace('Categories', description='Category operations')

@category_ns.route('/')
class CategoryList(Resource):
    
    @product_ns.marshal_list_with(category_model)
    def get(self):
        """List all categories"""
        return Category.query.all()
    
    @category_ns.expect(category_model)
    def post(self):
        """Create a new category"""
        data = category_ns.payload
        new_category = Category(
            name=data["name"],
            description=data["description"]
        )
        db.session.add(new_category)
        db.session.commit()
        
        return new_category, 201
    
@product_ns.route('/<int: id>')
class CategoryDetail(Resource):
    
    @product_ns.marshal_with(category_model)
    def get(self, id: int):
        """Retrieve a category by ID"""
        return Category.query.get_or_404(id)
    
    def delete(self, id: int):
        """Delete a category by ID"""
        product = Category.query.get_or_404(id) 
        db.session.delete(product)
        db.session.commit()
        
        return f"successfully deleted category with id {id}", 204