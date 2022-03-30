from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User, UserRoot, Mis  # 这句代码非常重要，
from apps import creat_app
from exts import db

app = creat_app()
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
