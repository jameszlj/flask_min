# coding:utf-8 
# author:james
# datetime:2019/9/11 16:24
#蓝图
from application import app
from web.controllers.api import api


app.register_blueprint(api, url_prefix='/api')