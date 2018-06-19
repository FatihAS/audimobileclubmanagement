from flask import Flask, render_template, send_from_directory
from app.session.controllers import check_login_session as check_login_session
from app.conn.conn import mysql

app = Flask(__name__,static_url_path='/static')

app.config.from_object('config')
mysql.init_app(app)

@app.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('static/images/', path)

@app.route('/icons/<path:path>')
def send_icon(path):
    return send_from_directory('static/icons/', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js/', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css/', path)

@app.route('/map_data/<path:path>')
def send_map_data(path):
    return send_from_directory('static/map_data/', path)

@app.errorhandler(404)
def not_found(error):
    return "error", 404

from app.home.controllers import home as home_controller
app.register_blueprint(home_controller)

from app.mod_auth.controllers import mod_auth as auth_module
app.register_blueprint(auth_module)

from app.tuyul.controllers import tuyul as tuyul_controller
app.register_blueprint(tuyul_controller)

from app.api.controllers import api as api_controller
app.register_blueprint(api_controller)