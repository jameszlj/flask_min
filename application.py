# coding:utf-8 
# author:james
# datetime:2019/9/11 14:17
import os

from flask import Flask
from flask_script import Manager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(
            import_name,
            template_folder=template_folder,
            root_path=root_path,
            static_folder=None
        )
        self.config.from_pyfile('config/base_setting.py')


app = Application(__name__, template_folder=os.getcwd() + '/web/templates', root_path=os.getcwd())
manager = Manager(app)

# from common.libs.UrlManager import UrlManager
"""
函数jiaja模板,暂时不用 
"""
# app.add_template_global(UrlManager.build_url, 'build_url')
# app.add_template_global(UrlManager.static_url, 'static_url')
# app.add_template_global(UrlManager.build_image_url, 'build_image_url')
