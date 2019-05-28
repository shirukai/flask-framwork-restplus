# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 18:43
数据库访问层
"""
from datetime import datetime

from pytz import timezone

from application import db, APIException
from application.database.models import User


def get_user_by_id(id):
    user = User.query.filter(User.id == id).one_or_none()
    if user:
        return user
    else:
        raise APIException(msg="User's id does not exist.")


def get_users(select_blogs=False):
    return [user.dict(select_blogs) for user in User.query.all()]


def create_user(name, role):
    user = User(name, role)
    db.session.add(user)
    db.session.commit()
    return user.dict()


def delete_user_by_id(id):
    user = get_user_by_id(id)
    user.blogs.delete()
    db.session.delete(user)
    db.session.commit()
    return "successfully deleted."


def update_user(id, name, role):
    user = get_user_by_id(id)
    user.name = name
    user.role = role
    user.modify_time = datetime.now(timezone('Asia/Shanghai')).replace(tzinfo=None)
    db.session.add(user)
    db.session.commit()
    return user.dict()
