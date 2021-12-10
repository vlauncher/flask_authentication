from auth_project import app,db
from auth_project.models import User

db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}