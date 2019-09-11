# coding:utf-8 
# author:james
# datetime:2019/9/11 14:07
import traceback

from flask_script import Server

from application import manager, app

import www

manager.add_command('runserver', Server(
    port=app.config['SERVER_PORT'],
    use_debugger=True
))


def main():
    manager.run()


if __name__ == '__main__':

    try:
        import sys
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()