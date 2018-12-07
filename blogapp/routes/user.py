from flask import request
from blogapp import app
from blogapp.models.user import User
from blogapp.routes.utils import res, require_login, require_admin, result


@app.route('/user/getAll', methods=['GET', 'POST'])
@require_login
def getAllUSer():
    users = User.query.all()
    users_dict = [user.to_dict() for user in users]
    return res(code=result.SUCC, data=users_dict)


@app.route('/user/delUser', methods=['GET', 'POST'])
@require_login
def delUser():
    username = request.args.get('username')
    try:
        User.delete.filter_by(username=username)
    except Exception:
        code = result.PARAM_ERR
        errmsg = 'failed to delete {}'.format(username)
    else:
        code = result.SUCC
    return res(code=code, errmsg=errmsg)


@app.route('/user/modify', methods=['GET', 'POST'])
@require_admin
def modify():
    username = request.args.get('username')
    password = request.args.get('password')
    new_password = request.args.get('newpassword')
    user = User.query.filter_by(username).first()
    if user.check_password(password):
        user.set_password(new_password)
        resCode = result.SUCC
    else:
        resCode = result.PARAM_ERR
        errmsg = 'Your old password was wrong!'
    return res(code=resCode, errmsg=errmsg)
