from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session
from app.tuyul.db import db
import json

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/tuyul',methods=['GET','POST'])
def tuyul_get_all():
    if request.method == "GET":
        return db.getAllTuyul()
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return db.addTuyul(data=content)

@api.route('/tuyul/edit',methods=['POST'])
def tuyul_edit():
    content = request.get_json(silent=True)
    return db.editTuyul(data=content)

@api.route('/tuyul/delete/<id>',methods=['GET'])
def tuyul_delete(id):
    return db.delTuyul(id=id)

@api.route('/tuyul/<id>',methods=['GET'])
def tuyul_get_one(id):
    return db.getTuyul(id=id)

@api.route('/sisatuyul',methods=['GET'])
def tuyul_get_avail():
    return db.getAllAvailableTuyul()
    
@api.route('/title',methods=['GET','POST'])
def title_get_all():
    return db.getAllTitle()

@api.route('/pusher',methods=['GET','POST'])
def pusher_get_all():
    if request.method == "GET":
        return db.getAllPusher()
    elif request.method == "POST":
        content = request.get_json(silent=True)
        return db.addPusher(data=content)

@api.route('/pusher/delete/<id>',methods=['GET'])
def pusher_delete(id):
    return db.delPusher(id=id)