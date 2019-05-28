# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-28 11:40
flask-apsheduler扩展
"""
from application.config import setting

if setting.ENABLE_SCHEDULER:
    from flask_apscheduler import APScheduler

    scheduler = APScheduler()
else:
    scheduler = None