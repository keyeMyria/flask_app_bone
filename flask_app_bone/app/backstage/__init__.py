from flask import Blueprint

backstage = Blueprint('backstage', __name__, template_folder='./templates')

from . import views