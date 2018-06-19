from flask import Blueprint, render_template, request, session, redirect
from app.session.controllers import check_login_session as check_login_session

admin = Blueprint('admin',__name__, url_prefix='/admin')

@admin.route('/',methods=['GET','POST'])
def admin_home():
    if check_login_session():
        # return "Sudah Login"
        return render_template("admin/dashboard.html")
    else:
        return redirect("/auth/signin")