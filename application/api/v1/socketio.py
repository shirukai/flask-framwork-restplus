# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-30 09:47
flask-socketio 例子
实时监控Flask所在主机内存使用情况
注意：需要再v1 __init__里引入此包用以初始化
"""
from flask import request
from flask_socketio import emit

from application.socketio import socketio
import psutil


def get_virtual_memory():
    """
    获取内存使用情况
    :return: dict
    """
    memory_info = psutil.virtual_memory()
    return {attr: getattr(memory_info, attr) for attr in dir(memory_info) if
            not attr.__contains__("_") and not isinstance(getattr(memory_info, attr), type(len))}


tasks = dict()


def background_task(sid):
    # add sid to tasks
    tasks[sid] = True
    while tasks[sid]:
        info = get_virtual_memory()
        print(info)
        socketio.emit("server_response", {'data': info}, namespace='/ws')
        socketio.sleep(2)
    if not tasks[sid]:
        tasks.pop(sid)


@socketio.on("connect", namespace="/ws")
def handle_connect():
    """
    handle connect
    :return:
    """
    sid = getattr(request, 'sid')
    socketio.start_background_task(background_task, sid)
    emit("connect", {'data': '连接成功'})


@socketio.on("disconnect", namespace="/ws")
def handle_disconnect():
    sid = getattr(request, 'sid')
    if sid in tasks:
        tasks[sid] = False
