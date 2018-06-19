from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session

mod_auth = Blueprint('mod_auth',__name__, url_prefix='/auth')

@mod_auth.route('/signin/',methods=['GET','POST'])
def signin():
    if check_login_session() is False:
        if request.method == "GET":
            return render_template("auth/index.html")
        else:
            if request.form['email'] == "mfatihas97@gmail.com" and request.form['password'] == "asdfgvcxz":
                session['email'] = request.form['email']
                return redirect("/admin")
            else:
                return render_template("auth/index.html")
    else:
        return redirect("/")

@mod_auth.route('/forgot/',methods=['GET','POST'])
def forgot():
    return render_template("auth/forgot.html")

@mod_auth.route('/register/',methods=['GET','POST'])
def register():
    return render_template("auth/register.html")

@mod_auth.route('/logout/',methods=['GET'])
def logout():
    session.pop('email')
    return redirect("/")