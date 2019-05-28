# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
user endpoints
"""

from flask import request
from flask_restplus import Resource

from application.api.v1.restplus import api
from application.api.v1.user import business
from application.api.v1.serializers import user, user_post, user_blogs

ns = api.namespace('user', description='Operations related to v1 user.')


@ns.route('/')
class UserCollection(Resource):
    @api.marshal_list_with(user)
    def get(self):
        """
        Returns list of user.
        """
        return business.get_users()

    @api.expect(user_post)
    def post(self):
        """
        Creates a new user.
        """
        data = request.get_json()
        return business.create_user(data['name'], data['role'])


@ns.route('/<user_id>')
class UserItem(Resource):
    @api.marshal_with(user)
    def get(self, blog_id):
        """
        Returns a user.
        """
        return business.get_user_by_id(blog_id).dict()

    @api.expect(user_post)
    def put(self, user_id):
        """
        Update user.
        """
        data = request.json
        return business.update_user(user_id, data['name'], data['role'])

    def delete(self, user_id):
        """
        Deletes user.
        """
        return business.delete_user_by_id(user_id)


@ns.route('/<user_id>/blogs')
class UserItemWithBlog(Resource):
    @api.marshal_with(user_blogs)
    def get(self, user_id):
        """
         Returns user with list of blog.
        """
        business.get_user_by_id(user_id).dict(select_blog=True)
