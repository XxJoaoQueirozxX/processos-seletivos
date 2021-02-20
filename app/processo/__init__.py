from flask import Blueprint

processo = Blueprint("processos", __name__)

from . import views
