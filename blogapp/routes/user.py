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
    return res(code=result.SUCC)


@app.route('/user/modify', methods=['GET', 'POST'])
@require_admin
def modify():
    username = request.args.get('username')
    password = request.args.get('password')
