# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 17:24
初始化数据库
"""
from flask_sqlalchemy import SQLAlchemy

# create db
db = SQLAlchemy()


def clear(flask_app):
    """
    删除所有表
    :param flask_app: app
    :return:
    """
    with flask_app.app_context():
        db.drop_all()


def init(flask_app):
    """
    创建所有表
    :param flask_app: app
    :return:
    """
    with flask_app.app_context():
        db.create_all()
