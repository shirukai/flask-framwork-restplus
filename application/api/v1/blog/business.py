# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 19:34
数据访问层
"""
from datetime import datetime

from pytz import timezone

from application import APIException, db
from application.api.v1.tag.business import get_tag_by_id
from application.database.models import Blog, Tag


def get_blog_by_id(id):
    blog = Blog.query.filter(Blog.id == id).one_or_none()
    if blog:
        return blog
    else:
        raise APIException(msg="Blog's id does not exist.")


def get_blogs():
    return [blog.dict() for blog in Blog.query.all()]


def create_blog(title, context, user_id, tags):
    blog = Blog(title=title, context=context, user_id=user_id)
    for tag_id in tags:
        tag = get_tag_by_id(tag_id)
        blog.tags.append(tag)
    db.session.add(blog)
    db.session.commit()
    return blog.dict()


def delete_blog_by_id(id):
    blog = get_blog_by_id(id)
    db.session.delete(blog)
    db.session.commit()
    return "successfully deleted."


def update_blog(id, title, context,tags):
    blog = get_blog_by_id(id)
    blog.title = title
    blog.context = context
    blog.modify_time = datetime.now(timezone('Asia/Shanghai')).replace(tzinfo=None)
    for tag_id in tags:
        tag = get_tag_by_id(tag_id)
        blog.tags.append(tag)
    db.session.add(blog)
    db.session.commit()
    return blog.dict()
