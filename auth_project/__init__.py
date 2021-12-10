import os
from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from .pages import pages as pagesblueprint
app.register_blueprint(pagesblueprint)
from .auth import auth as authBlueprint
app.register_blueprint(authBlueprint)

from . import app