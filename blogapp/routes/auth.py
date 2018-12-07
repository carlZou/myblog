from flask import request, session

from blogapp import app, db
from blogapp.models.user import User
from blogapp.routes.utils import res, result


@app.route('/signin', methods=['POST'])
def signin():
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        code = result.SUCC
        session['username'] = username
        if username == 'carl':
            session['admin'] = username
    else:
        code = result.FAIL
        errmsg = 'please check your username or password and try again!'
    return res(code=code, errmsg=errmsg)


@app.route('/signup', methods=['POST'])
def signup():
    username = request.args.get('username')
    password = request.args.get('password')
    repassword = request.args.get('repassword')
    if username is not None and User.query.filter_by(username=username).first() is not None:
        code = result.PARAM_ERR
        errmsg = 'This username already been used！'
    else:
        if password is not None and password != repassword:
            code = result.SUCC
            errmsg = 'please check you password, it seems like diff!'
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            code = result.SUCC
    return res(code=code, errmsg=errmsg)


@app.route('/signout')
def signout():
    if 'username' in session:
        session.pop('username')
        code = result.SUCC
    else:
        code = result.NOT_LOGIN
        errmsg = 'You haven not sign in yet !'
    return res(code=code, errmsg=errmsg)
