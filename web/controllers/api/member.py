# coding:utf-8 
# author:james
# datetime:2019/9/11 16:36
import traceback
import uuid

import pymysql
from flask import request, jsonify

from application import app
from common.libs.ApiResult import ApiResult
from common.libs.MemberService import MemberService
# from web.controllers.api import api


def login():
    result = ApiResult()
    req = request.values
    print(req)
    id = str(uuid.uuid1())
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        result.code = -1
        result.msg = "需要code"
        return result

    openid = MemberService.get_wechat_openid(code)
    if openid is None:
        result.code = -1
        result.msg = "调用微信出错"
        return result

    nick_name = req['nickName'] if 'nickName' in req else ''
    sex = req['gender'] if 'gender' in req else 0
    avatar = req['avatarUrl'] if 'avatarUrl' in req else ''
    city = req['city'] if 'city' in req else ''
    province = req['province'] if 'province' in req else ''
    country = req['country'] if 'country' in req else ''

    try:
        conn = pymysql.connect(host=app.config['DB_CONFIG']['host'], port=app.config['DB_CONFIG']['port'], user=app.config['DB_CONFIG']['user'],
                               passwd=app.config['DB_CONFIG']['passwd'], db=app.config['DB_CONFIG']['db'], charset=app.config['DB_CONFIG']['charset'])
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        select_sql = """
            SELECT 
                id,
                salt,
                status
            from `user`
            where open_id =%s
            AND source = %s 
        """
        cursor.execute(select_sql,[openid, 1])
        bind_info=cursor.fetchone()
        if not bind_info:
            salt = MemberService.gene_salt()
            insert_sql = """
                    INSERT INTO `user` (
                        id,
                        nick_name,
                        sex,
                        avatar,
                        salt,
                        source,
                        open_id,
                        city,
                        province,
                        country,
                        add_time,
                        update_time 
                      )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        NOW(),
                        NOW()
                    ) 
            """
            cursor.execute(insert_sql, [id,
                                        nick_name,
                                        sex,
                                        avatar,
                                        salt,
                                        1,
                                        openid,
                                        city,
                                        province,
                                        country
                                        ])
            conn.commit()
            bind_info = {"id": id,
                         "salt": salt,
                         "status": 1}

        token = "%s#%s" % (MemberService.gene_auth_code(bind_info), bind_info["id"])
        result.code = 200
        result.msg = '操作成功~'
        result.data = {'token': token}
    except Exception as e:
        print(e)
        result.code = -1
        result.msg = traceback.format_exc()
    finally:
        cursor.close()
        conn.close()
        return result


def check_reg():
    result = ApiResult()
    req = request.values
    code = req['code'] if 'code' in req else ''
    if not code or len(code) < 1:
        result.code = -1
        result.msg = "需要code"
        return result

    openid = MemberService.get_wechat_openid(code)
    if openid is None:
        result.code = -1
        result.msg = "调用微信出错"
        return result

    try:
        conn = pymysql.connect(host=app.config['DB_CONFIG']['host'], port=app.config['DB_CONFIG']['port'], user=app.config['DB_CONFIG']['user'],
                               passwd=app.config['DB_CONFIG']['passwd'], db=app.config['DB_CONFIG']['db'], charset=app.config['DB_CONFIG']['charset'])
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        select_sql = """
            SELECT 
                id,
                salt,
                status
            from `user`
            where open_id =%s
            AND source = %s 
        """
        cursor.execute(select_sql,[openid, 1])
        bind_info = cursor.fetchone()
        if not bind_info:
            result.code = -1
            result.msg = "未绑定"
            return result
        token = "%s#%s" % (MemberService.gene_auth_code(bind_info), bind_info["id"])
        result.code = 200
        result.msg = '操作成功~'
        result.data = {'token': token}
    except Exception as e:
        print(e)
        result.code = -1
        result.msg = traceback.format_exc()
    finally:
        cursor.close()
        conn.close()
        return result
