from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session

home = Blueprint('home',__name__, url_prefix='/')

@home.route('/',methods=['GET','POST'])
def landingPage():
    return render_template("home/index.html")