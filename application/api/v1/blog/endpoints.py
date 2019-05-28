# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
blog endpoints
"""

from flask import request
from flask_restplus import Resource

from application.api.v1.serializers import blog, blog_post
from application.api.v1.restplus import api
from application.api.v1.blog import business

ns = api.namespace('blog', description='Operations related to v1 blog.')


@ns.route("/")
class BlogCollection(Resource):
    @api.marshal_list_with(blog)
    def get(self):
        """
        Returns list of blog.
        """
        return business.get_blogs()

    @api.expect(blog_post)
    def post(self):
        """
        Creates a new blog.
        """
        data = request.get_json()
        return business.create_blog(data['title'], data['context'], data['user_id'], data['tags'])


@ns.route("/<blog_id>")
class BlogItem(Resource):
    @api.marshal_with(blog)
    def get(self, blog_id):
        """
        Returns a blog.
        """
        return business.get_blog_by_id(blog_id).dict()

    @api.expect(blog_post)
    def put(self, blog_id):
        """
        Update blog.
        """
        data = request.json
        return business.update_blog(blog_id, data['title'], data['context'], data['tags'])

    def delete(self, blog_id):
        """
        Deletes blog.
        """
        return business.delete_blog_by_id(blog_id)
