from app import app, db
from app.models import Todo
from flask_script import Manager

manager = Manager(app)

@manager.command
def save():
    todo = Todo('study flask')
    db.session.add(todo)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
