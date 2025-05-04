# /home/axlee/Desktop/AI_Scrum_Agile/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False

    # --- Add specific configurations for AIAO components ---
    # Example for Jira (replace with actual env variables in .env)
    JIRA_URL = os.environ.get('JIRA_URL')
    JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
    JIRA_API_TOKEN = os.environ.get('JIRA_API_TOKEN')

    # Example for Slack
    SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

    # Example for Database (if needed later)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    # Use a separate test database if needed
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Production configuration."""
    # Ensure sensitive keys are definitely set from environment
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for production")
    # Add other production-specific settings


# Dictionary to access config classes by name
config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
)

# Function to get the appropriate config object
def get_config():
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    return config_by_name[config_name]
