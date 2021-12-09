import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
from .pages import pages as pagesblueprint
app.register_blueprint(pagesblueprint)
from .auth import auth as authBlueprint
app.register_blueprint(authBlueprint)

from . import app