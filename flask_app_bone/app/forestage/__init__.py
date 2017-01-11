from flask import Blueprint

forestage = Blueprint('forestage', __name__, template_folder='./templates')

from . import views