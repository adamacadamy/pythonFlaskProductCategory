def register_routes(api):
    from app.routes.products import product_ns
    from app.routes.categories import category_ns
    
    api.add_namespace(product_ns)
    api.add_namespace(category_ns)