# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-28 20:01
serializers用以规范请求参数和返回值
"""
from flask_restplus import fields

from application.api.v1.restplus import api

user = api.model('User', {
    'id': fields.String(required=True, description='User id'),
    'name': fields.String(required=True, description='User name'),
    'role': fields.Integer(required=True, description='User role'),
})

tag = api.model('Tag', {
    'id': fields.String(required=True, description='Tag id'),
    'name': fields.String(required=True, description='Tag name')
})

blog = api.model('Blog', {
    'title': fields.String(required=True, description='Blog title'),
    'context': fields.String(required=True, description='Blog context'),
    'owner': fields.Nested(user),
    'tags': fields.List(fields.Nested(tag)),
    'create_time': fields.String(),
    'modify_time': fields.String()
})

blog_post = api.model('Blog post', {
    'title': fields.String(required=True, description='Blog title'),
    'context': fields.String(required=True, description='Blog context'),
    'user_id': fields.String(required=True, description='Blog owner id'),
    'tags': fields.List(fields.String),
})

user_post = api.model('User post.', {
    'name': fields.String(required=True, description='User name'),
    'role': fields.Integer(required=True, description='User role')
})

user_blogs = api.model('User blogs.', {
    'name': fields.String(required=True, description='User name'),
    'role': fields.Integer(required=True, description='User role'),
    'blogs': fields.List(fields.Nested(blog))
})

tag_post = api.model('Tag post.', {
    'name': fields.String(required=True, description='Tag name')
})

tag_blogs = api.model('Tag with list of blog.', {
    'id': fields.String(required=True, description='Tag id'),
    'name': fields.String(required=True, description='Tag name'),
    'blogs': fields.List(fields.Nested(blog))
})
