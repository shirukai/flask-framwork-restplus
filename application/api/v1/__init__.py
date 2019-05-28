# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:23

"""
from flask import Blueprint

from application.api.v1 import socketio
from application.api.v1.blog.endpoints import ns as blog_ns
from application.api.v1.user.endpoints import ns as user_ns
from application.api.v1.tag.endpoints import ns as tag_ns
from application.api.v1.restplus import api


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__, url_prefix="/api/v1")
    api.init_app(bp_v1)
    api.add_namespace(blog_ns)
    api.add_namespace(user_ns)
    api.add_namespace(tag_ns)
    return bp_v1
