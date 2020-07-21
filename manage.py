from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Comment, Category, Pitch
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell #shell is used to test features in our app and for debugging
def make_shell_context():
    return dict(app = app,db = db,User = User, Comment= Comment, Category=Category, Pitch=Pitch)

if __name__ == '__main__':
    manager.run()
