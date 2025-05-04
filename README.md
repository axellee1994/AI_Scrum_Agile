# AI-Driven Agile Orchestrator (AIAO)

## Project Goal

To develop an AI system capable of performing the core functions of a Scrum Master and automating key Agile/Scrum ceremonies and artifact management, aiming to enhance team efficiency and potentially reduce reliance on manual process facilitation.

*(Based on the initial concept - can be expanded)*

## Project Structure

This project uses a Python/Flask framework following a Model-View-Controller (MVC) inspired pattern:

```
/AI_Scrum_Agile/
|-- aiao/                     # Main application package
|   |-- __init__.py           # App factory (create_app)
|   |-- controllers/          # Handles incoming requests (API endpoints, dashboard routes)
|   |   |-- __init__.py
|   |   |-- dashboard_controller.py
|   |   |-- api_controller.py
|   |-- models/               # Data representation, business logic, data access
|   |   |-- __init__.py
|   |   |-- task.py
|   |   |-- sprint.py
|   |   |-- metrics.py
|   |-- services/             # Core logic: AI, data processing, external API interaction
|   |   |-- __init__.py
|   |   |-- data_ingestion/     # Connectors (Jira, Git, Slack etc.)
|   |   |   |-- __init__.py
|   |   |   |-- jira_connector.py
|   |   |-- processing/         # Data cleaning, feature engineering
|   |   |   |-- __init__.py
|   |   |   |-- feature_extractor.py
|   |   |-- ai_models/          # Predictive models, NLP, optimization
|   |   |   |-- __init__.py
|   |   |   |-- predictive_analytics.py
|   |   |   |-- nlp_module.py
|   |-- views/                # Presentation logic (Jinja2 templates)
|   |   |-- __init__.py
|   |   |-- templates/
|   |   |   |-- base.html
|   |   |   |-- dashboard.html
|   |   |-- static/             # CSS, JavaScript, images
|   |       |-- css/ style.css
|   |       |-- js/ script.js
|   |-- utils/                # Helper functions, constants
|       |-- __init__.py
|       |-- helpers.py
|-- tests/                    # Unit and integration tests
|   |-- __init__.py
|   |-- test_controllers.py
|   |-- test_services.py
|-- .env                      # Environment variables (API keys, secrets) - **Gitignored**
|-- .gitignore                # Files/directories ignored by Git
|-- config.py                 # Application configuration settings
|-- requirements.txt          # Python dependencies
|-- run.py                    # Application entry point
|-- README.md                 # This file
```

## Setup Instructions

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd AI_Scrum_Agile
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Copy the structure from `config.py` for necessary environment variables (like `SECRET_KEY`, `JIRA_URL`, etc.). Start with just `SECRET_KEY` if you don't have API keys yet.
    ```
    # .env file
    SECRET_KEY='a_very_secret_key_change_me'
    FLASK_CONFIG='development' # Or 'production', 'testing'
    # Add other keys as needed, e.g.:
    # JIRA_URL=https://your-domain.atlassian.net
    # JIRA_USERNAME=your-email@example.com
    # JIRA_API_TOKEN=your-api-token
    ```
    *Note: Ensure this file is listed in your `.gitignore`.* 

## Running the Application

Once set up, you can run the Flask development server:

```bash
python3 run.py
```

The application should be accessible at `http://127.0.0.1:5000` or `http://0.0.0.0:5000`. You should see the welcome message defined in `aiao/__init__.py`.

## Next Steps

*   Implement basic dashboard routes in `dashboard_controller.py`.
*   Define data models in `models/`.
*   Develop data ingestion connectors in `services/data_ingestion/`.
*   Build out AI/ML components in `services/ai_models/`.
*   Create tests in the `tests/` directory.
