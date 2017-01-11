# coding=utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# bootstrap = Bootstrap()

db = SQLAlchemy()


def create_app(config=None, app_name=None):

	app = Flask(__name__)
	db.init_app(app)


	from .forestage import forestage as forestage_blueprint
	app.register_blueprint(forestage_blueprint, url_prefix='/')

	from .admin import admin as admin_blueprint
	app.register_blueprint(admin_blueprint, url_prefix='/admin')

	from .backstage import backstage as backstage_blueprint
	app.register_blueprint(backstage_blueprint, url_prefix='/backstage')

	from .api.api_1_0 import api_1_0 as api_1_0_blueprint
	app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v_1_0')


	return app



