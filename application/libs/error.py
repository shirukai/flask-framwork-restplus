# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 19:43
异常请求处理
"""
from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    msg = 'sorry,unknown error!'
    code = 500

    def __init__(self, msg=None, code=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            code=self.code,
            request=request.method + ' ' + self.get_url_no_param(),
            status="failed"
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
