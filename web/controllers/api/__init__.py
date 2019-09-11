# coding:utf-8 
# author:james
# datetime:2019/9/11 14:58
from flask import Blueprint

api = Blueprint('api', __name__)
from web.controllers.api.member import *


@api.route('/')
def index():
    return "Mina Api V1.0"