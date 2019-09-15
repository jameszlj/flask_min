#-*- coding:utf-8 -*-
# import random
# import base64
# from itsdangerous import URLSafeTimedSerializer as usts


class ApiResult():
    def __init__(self):
        self.code = 0
        self.data = None
        self.msg = ""
        self.content_type = "application/json"

    def to_content(self):
        if self.content_type == "application/json":
            import json
            temp = dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__') and not callable(getattr(self, name)))
            return json.dumps(temp)
        else:
            return self.data
