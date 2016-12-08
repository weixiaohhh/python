from app import app
from app.model import ToDo
from flask_script import Manager,Shell
from app import db


manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, ToDo=ToDo)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def save():

    todo = ToDo(content="study flask")
    db.session.add(todo)
    db.session.commit()




if __name__ == '__main__':
    manager.run()