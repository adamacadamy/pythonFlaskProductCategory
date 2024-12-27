import nest_asyncio
from werkzeug.serving import run_simple
from app import create_app
 
app = create_app()
 

if __name__ == "__main__":
    app.run(debug=True)