from flask import jsonify


def res(succ, code, errmsg):
    return jsonify(succ=succ, code=code, errmsg=errmsg)
