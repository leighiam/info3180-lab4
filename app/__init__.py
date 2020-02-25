from flask import Flask
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'
UPLOAD_FOLDER = './app/static/uploads'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'
"""app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER""" 

app = Flask(__name__)
app.config.from_object(__name__)
csrf.init_app(app)
from app import views
