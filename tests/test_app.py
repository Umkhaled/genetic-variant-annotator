
import sys
import os

# Add the app_folder directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app_folder')))

from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

