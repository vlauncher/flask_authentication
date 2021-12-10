from auth_project import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30),nullable=False)
    last_name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(130),unique=True,nullable=False)
    username = db.Column(db.String(30),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f'User({self.first_name} {self.last_name})'