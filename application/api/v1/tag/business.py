# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-28 10:07
tag数据访问层
"""

from application import APIException, db
from application.database.models import Tag


def get_tag_by_id(id):
    tag = Tag.query.filter(Tag.id == id).one_or_none()
    if tag:
        return tag
    else:
        raise APIException(msg="Tag's id does not exist.")


def get_tags():
    return [tag.dict() for tag in Tag.query.all()]


def create_tag(name):
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return tag.dict()


def delete_tag_by_id(id):
    tag = get_tag_by_id(id)
    db.session.delete(tag)
    db.session.commit()
    return "successfully deleted."


def update_tag(id, name):
    tag = get_tag_by_id(id)
    tag.name = name
    db.session.add(tag)
    db.session.commit()
    return tag.dict()
