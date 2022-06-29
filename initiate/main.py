#Entrypoint of the app
import sys
from pathlib import Path
from internal.app import backend_app  

# Get the base dir to correctly import the main backend app
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

# Generate an instance of the main app
app = backend_app()