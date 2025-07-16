# Import external libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create app function
# Returns app

def create_app():
    app = Flask(__name__)
    
    # Import views from views.py
    from .views import views
    
    # Register blueprints
    app.register_blueprint(views, url_prefix="/")
    
    
    return app