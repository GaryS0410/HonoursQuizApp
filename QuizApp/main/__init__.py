from flask import Blueprint

bp = Blueprint('main', __name__)

from QuizApp.main import routes