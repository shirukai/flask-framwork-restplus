# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
tag endpoints
"""

from flask import request
from flask import jsonify
from flask_restplus import Resource

from application.api.v1.restplus import api
from application.api.v1.tag import business
from application.api.v1.serializers import tag, tag_post, tag_blogs

ns = api.namespace('tag', description='Operations related to v1 tag.')


@ns.route('/')
class TagCollection(Resource):
    @api.marshal_list_with(tag)
    def get(self):
        """
        Returns list of tag.
        """
        return business.get_tags()

    @api.expect(tag_post)
    def post(self):
        """
        Creates a new tag.
        """
        data = request.get_json()
        return business.create_tag(data['name'])


@ns.route('/<tag_id>')
class TagItem(Resource):
    @api.marshal_with(tag)
    def get(self, tag_id):
        """
        Returns a tag.
        """
        return business.get_tag_by_id(tag_id).dict()

    @api.expect(tag_post)
    def put(self, tag_id):
        """
        Update tag.
        """
        data = request.json
        return business.update_tag(tag_id, data['name'])

    def delete(self, tag_id):
        """
        Deletes tag.
        """
        return business.delete_tag_by_id(tag_id)


@ns.route('/<tag_id>/blogs')
class TagItemWithBlog(Resource):
    @api.marshal_with(tag_blogs)
    def get(self, tag_id):
        """
         Returns tag with list of blog.
        """
        business.get_tag_by_id(tag_id).dict(select_blog=True)
