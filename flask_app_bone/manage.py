#!/env/bin/env python3
# coding=utf-8

import os

from app import app

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


inst = app.create_app()
manager = Manager(inst)
migrate = Migrate(app, app.db)


def main():
	manager.run()

if __name__ == '__main__':
	main()