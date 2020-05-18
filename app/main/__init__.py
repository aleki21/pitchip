from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error

bootstrap = Bootstrap()

