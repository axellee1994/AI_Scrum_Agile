# /home/axlee/Desktop/AI_Scrum_Agile/aiao/__init__.py
from flask import Flask
from config import get_config, Config # Import base Config for type hint

def create_app(config_name: str = 'default') -> Flask:
    """
    Application factory function.
    Creates and configures the Flask application.
    """
    app = Flask(__name__)

    # Load configuration
    config_object = get_config()
    app.config.from_object(config_object)

    # Initialize extensions (e.g., db, migrate, login_manager) here if needed
    # Example:
    # from .extensions import db
    # db.init_app(app)

    # Register blueprints (routes)
    # Example:
    # from .controllers.dashboard_controller import dashboard_bp
    # app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    # Add a simple root route for now
    @app.route('/')
    def index():
        return "Welcome to the AI-Driven Agile Orchestrator (AIAO)!"

    # You can add more initialization logic here

    return app