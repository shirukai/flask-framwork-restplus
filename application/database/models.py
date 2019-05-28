# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 17:38
数据库表模型
提供三张表模型：用户表、博客表、标签表

用户与博客为一对多关系
博客与标签为多多多关系
关于模型声明参考：http://docs.jinkan.org/docs/flask-sqlalchemy/models.html
"""
import uuid
from datetime import datetime
from pytz import timezone

from application import db

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'))
                )


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False)
    blogs = db.relationship('Blog', backref='User', lazy='dynamic')

    USER = 0
    ADMIN = 1

    def __init__(self, name, role):
        self.id = str(uuid.uuid1())
        self.name = name
        self.role = role

    def dict(self, select_blog=False):
        user = {
            "id": self.id,
            "name": self.name,
            "role": self.role
        }
        if select_blog:
            user['blogs'] = [blog.dict() for blog in self.blogs]
        return user

    def __repr__(self):
        return 'User %r' % self.name


class Blog(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    context = db.Column(db.Text)
    tags = db.relationship('Tag',
                           secondary=tags,
                           backref=db.backref('pages', lazy='dynamic'))
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, context, user_id):
        self.id = str(uuid.uuid1())
        self.title = title
        self.context = context
        self.user_id = user_id
        self.create_time = datetime.now(timezone('Asia/Shanghai')).replace(tzinfo=None)

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'context': self.context,
            'owner': self.User.dict(),
            'tags': [tag.dict() for tag in self.tags],
            'create_time': format_time(self.create_time),
            'modify_time': format_time(self.modify_time)
        }

    def __repr__(self):
        return 'Blog %r' % self.title


class Tag(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.id = str(uuid.uuid1())
        self.name = name

    def dict(self, select_blog=False):
        tag = {
            'id': self.id,
            'name': self.name
        }
        if select_blog:
            tag['blogs'] = []
        return tag

    def __repr__(self):
        return 'Tag %r' % self.name


def format_time(time, fmt="%Y-%m-%d %H:%M:%S"):
    if time:
        return time.strftime(fmt)
    else:
        ""
