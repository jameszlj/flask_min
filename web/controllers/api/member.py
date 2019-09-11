# coding:utf-8 
# author:james
# datetime:2019/9/11 16:36
from web.controllers.api import api
@api.route("member/login", methods=['GET', 'POST'])
def login():
    return "login"