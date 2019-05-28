# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:35
配置
"""
FLASK_DEBUG = True

# set host and port
FLASK_SERVER_HOST = '0.0.0.0'
FLASK_SERVER_PORT = 5000

# set database
SQLALCHEMY_DATABASE_URI = 'sqlite:///../application.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# set socketio
ENABLE_SOCKETIO = True
SOCKETIO_ASYNC_MODE = 'threading'

# set scheduler
ENABLE_SCHEDULER = False

# set restplus
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
