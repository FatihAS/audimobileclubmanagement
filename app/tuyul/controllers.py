from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session
from app.tuyul.db import db
import json

tuyul = Blueprint('tuyul',__name__, url_prefix='/admin')

@tuyul.route('/',methods=['GET','POST'])
def dashboard():
    if check_login_session():
        if request.method == "GET":
            return render_template("admin/dashboard.html")
        else:
            return redirect("/")    
    else:
        return redirect("/")

@tuyul.route('/tuyul-list-tuyul',methods=['GET','POST'])
def list_tuyul():
    if check_login_session():
        if request.method == "GET":
            title = db.getAllTitle()
            return render_template("admin/list-tuyul.html",title=json.loads(title))
        else:
            return redirect("/")    
    else:
        return redirect("/")

@tuyul.route('/edit-tuyul/<id>',methods=['GET','POST'])
def edit_tuyul(id):
    if check_login_session():
        if request.method == "GET":
            tuyul = db.getTuyul(id=id)
            title = db.getAllTitle()
            return render_template("admin/edit-tuyul.html",tuyul=json.loads(tuyul),title=json.loads(title))
        else:
            return redirect("/")    
    else:
        return redirect("/")


@tuyul.route('/tuyul-pusher',methods=['GET','POST'])
def pusher():
    if check_login_session():
        if request.method == "GET":
            return render_template("admin/pusher.html")
        else:
            return redirect("/")    
    else:
        return redirect("/")