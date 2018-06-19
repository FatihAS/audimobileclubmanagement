from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session
from app.tuyul.db import db

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/tuyul',methods=['GET','POST'])
def tuyul_get_all():
    return db.getAllTuyul()
    