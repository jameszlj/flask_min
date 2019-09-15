# coding:utf-8 
# author:james
# datetime:2019/9/11 14:24
SERVER_PORT = 9000
DEBUG = False
NOVEL_APP = {
    'appid': 'wx14a93595ef117322',
    'appkey': '4f67c85b8cddeaf187877f03c6b58177'
}

DB_CONFIG={
    'host': "localhost",
    'user': "root",
    'passwd': "root",
    'db': "novel",
    'port': 3306,
    'charset': 'utf8'
}

UPLOAD = {
    'ext':['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url':'/static/upload/'
}


APP = {
    'domain':'http://127.0.0.1:9000'
}