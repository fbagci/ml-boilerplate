import json
import os

from flask import Flask, request, jsonify
from jsonschema import validate

from src.project_name.project_name import project_class
from src.project_name.core.utils.convert import converter
from src.project_name.core.utils.rw import rw
from src.project_name.core.utils.datetime import dt


# Initialize flask app
app = Flask(__name__)

# Initialize objects
config = rw.get_config()
project = project_class()

# Initialize constants
BODY_SCHEMA = {
    "type": "object",
    "properties": { "image": { "type": "string" } }
}
LOG_BASE_FOLDER = "log"

# Initialize constants from config
CONSOLE_LOG_ENABLED = config["project"]["LOG"]["CONSOLE"]["ENABLE"].lower() == "true"
TIME_FORMAT = config["project"]["LOG"]["TIME_FORMAT"]
LOG_FULL_PATH = os.path.join(LOG_BASE_FOLDER, dt.new_strftime(TIME_FORMAT)) 

def create_log_dir():
    """
    Generate new log dir
    """
    # Generate log directory if not exists
    if not (LOG_BASE_FOLDER in os.listdir()):
        os.mkdir(LOG_BASE_FOLDER)
    # Generate log directory
    os.mkdir(LOG_FULL_PATH)

def init():
    """
    Generate log directory
    """
    # Generate log directory
    create_log_dir()

def body_is_valid(body):
    """
    Validate request body
    """
    try:
        validate(instance=body, schema=BODY_SCHEMA)
        return True
    except:
        return False

@app.route("/predict", methods=["POST"])
def predict():
    """
    Runs project with input in body
    """
    # Parse body
    body = json.loads(request.data)
    # Validate body
    if not body_is_valid(body):
        return "Request body is incorrect. Please check readme!"
    # Run project
    prediction = project.run_project()
    return jsonify({"prediction":prediction})

if __name__ == "__main__":
    init()
    runapp = app.run(host = "0.0.0.0",
                    threaded = True,
                    port = config["SERVICE"]["PORT"])