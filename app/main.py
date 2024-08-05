from flask import Blueprint

main = Blueprint('main', __name__)

# Import routes to associate them with the blueprint
from . import routes