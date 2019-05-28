# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 16:48
应用初始化
"""
import logging.config
import os

from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

from application.apsheduler import scheduler
from application.config.scheduler import SchedulerConfig
from application.database import db
from application.libs.error import APIException
from application.libs.ok import api_success_handler
from application.socketio import socketio
from application.api.v1 import create_blueprint_v1
from application.config import setting

# 设置模板文件以及静态文件路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(BASE_DIR, 'application/templates')
static_dir = os.path.join(templates_dir, 'static')
logging_conf_path = os.path.normpath(os.path.join(BASE_DIR, 'application/config/logging.conf'))

app = Flask(__name__, static_folder=static_dir)


@app.route("/")
def index():
    return render_template("index.html")


def configure_app(flask_app):
    logging.config.fileConfig(logging_conf_path)
    flask_app.config.from_object("application.config.setting")


def initialize_app(flask_app):
    """
    初始化app
    :return:
    """
    configure_app(flask_app)
    flask_app.register_blueprint(blueprint=create_blueprint_v1())

    # init db
    db.init_app(flask_app)

    # init socket
    if setting.ENABLE_SOCKETIO:
        socketio.init_app(app=flask_app, async_mode=setting.SOCKETIO_ASYNC_MODE)

    # init scheduler
    if setting.ENABLE_SCHEDULER:
        flask_app.config.from_object(SchedulerConfig)
        scheduler.init_app(app=flask_app)
        scheduler.start()


initialize_app(app)


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        return APIException(e.description, e.code)
    if isinstance(e, KeyError):
        msg = "Method needs the parameter '%s',KeyError Exception!" % e.args
        return APIException(msg)
    else:
        return APIException(str(e))

