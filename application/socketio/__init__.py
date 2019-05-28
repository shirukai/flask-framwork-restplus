# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 16:51
socketio 扩展
"""
from application.config import setting

if setting.ENABLE_SOCKETIO:
    from flask_socketio import SocketIO

    socketio = SocketIO()
else:
    socketio = None
