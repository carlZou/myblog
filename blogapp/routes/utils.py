from enum import unique, IntEnum
from functools import wraps

from flask import jsonify, session


@unique
class result(IntEnum):
    SUCC = 200
    FAIL = 300
    PARAM_ERR = 310
    NO_AUTH = 205
    NOT_LOGIN = 204
    SEVER_ERR = 500


def res(code, errmsg='', data=''):
    succ = False
    if code == 200:
        succ = True
    return jsonify(succ=succ, code=code, errmsg=errmsg, data=data)


def require_login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        user = session.get('username')
        if not user:
            return res(False, 405, 'no auth')
        else:
            return func(*args, **kwargs)
    return inner


def require_admin(func):
    @wraps(func)
    def inner(*args, **kwargs):
        admin = session.get('admin')
        if not admin:
            return res(False, 405, 'no auth')
        else:
            return func(*args, **kwargs)
    return inner
