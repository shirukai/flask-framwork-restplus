# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-28 15:11
应用入口
"""
from flask_script import Manager

from application import app, database
from application.socketio import socketio
from application.config import setting

manager = Manager(app)


@manager.command
def runserver(host=None, port=None):
    if not host:
        host = setting.FLASK_SERVER_HOST
    if not port:
        port = setting.FLASK_SERVER_PORT
    if setting.ENABLE_SOCKETIO:
        socketio.run(app, host=host, port=port, debug=setting.FLASK_DEBUG)
    else:
        app.run(host, port, debug=setting.FLASK_DEBUG)


@manager.command
def init_db():
    database.init(app)


@manager.command
def clear_db():
    database.clear(app)


if __name__ == '__main__':
    manager.run()
