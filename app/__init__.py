from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)
# Initializing flask extensions
bootstrap.init_app(app)

from app import views
from app import error
