# /home/axlee/Desktop/AI_Scrum_Agile/run.py
import os
from aiao import create_app

# Get the configuration name from environment variable or use default
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)

if __name__ == '__main__':
    # Use Flask's built-in server
    # Debug mode will be enabled if DevelopmentConfig is used
    app.run(debug=app.config['DEBUG'])