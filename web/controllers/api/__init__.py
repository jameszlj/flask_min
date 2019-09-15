# coding:utf-8 
# author:james
# datetime:2019/9/11 14:58
import traceback

from flask import Blueprint, app, Response

from common.libs.ApiResult import ApiResult
from web.controllers.api import realization

api = Blueprint('api', __name__)
# from web.controllers.api.member import *


@api.route('/<module_name>/<function_name>/', methods=['GET', 'POST'], strict_slashes=False)
def index(module_name,function_name):
    result = ApiResult()
    func = None
    if hasattr(realization, module_name):
        module = getattr(realization, module_name)
        if hasattr(module, function_name):
            func = getattr(module, function_name)
        else:
            result.code = -1
            result.message = r"function <%s> not exist in module <%s>" % (function_name, module_name)
    else:
        result.code = -1
        result.message = r"module <%s> not exist" % (module_name)
    try:
        if func:
            result = func()
    except Exception:
        result.code = -1
        result.message = traceback.format_exc()
    finally:
        if isinstance(result, Response):
            error = ApiResult()
            error.code = result.status_code
            error.message = result.__repr__()
            result = error
            # return 404
        if isinstance(result, ApiResult):
            return Response(result.to_content(), mimetype=result.content_type)
        else:
            return result