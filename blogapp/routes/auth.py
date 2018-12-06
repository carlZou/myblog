from flask import request, session

from blogapp import app, db
from blogapp.models.user import getuser, User
from blogapp.routes.utils import res


@app.route('/signin', methods=['POST'])
def signin():
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        success = True
        code = 200
        errMsg = ''
    else:
        session['username'] = username
        success = False
        code = 100
        errMsg = 'please check your username or password and try again!'
    return res(success, code, errMsg)


@app.route('/signup', methods=['POST'])
def signup():
    username = request.args.get('username')
    password = request.args.get('password')
    repassword = request.args.get('repassword')
    succ = False
    if username is not None and User.query.filter_by(username=username).first() is not None:
        code = 101
        errmsg = 'This username already been used！'
    else:
        if password is not None and password != repassword:
            code = 100
            errmsg = 'please check you password, it seems like diff!'
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            succ = True
            code = 200
            errmsg = ''
    return res(succ, code, errmsg)


@app.route('/user/getAll', methods=['GET', 'POST'])
def getAllUSer():
    succ = False
    code = 405
    errmsg = session.get('username', 'not set')
    return res(succ, code, errmsg)
