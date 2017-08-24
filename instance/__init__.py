from flask import Blueprint

shopper = Blueprint('shopper', __name__)

from . import views