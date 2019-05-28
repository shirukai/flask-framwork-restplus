# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-21 14:37
APScheduler配置
"""
from datetime import date, datetime

from apscheduler.jobstores.memory import MemoryJobStore
# from apscheduler.jobstores.mongodb import MongoDBJobStore
# from apscheduler.jobstores.redis import RedisJobStore
# from apscheduler.jobstores.rethinkdb import RethinkDBJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.jobstores.zookeeper import ZooKeeperJobStore
# from apscheduler.triggers.cron import CronTrigger
from flask_apscheduler.auth import HTTPBasicAuth


def print_test(name):
    print(name)


class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'application.config.scheduler:print_test',
            'args': ('joke',),
            'trigger': 'interval',
            'seconds': 1,
            # 'start_date': '2019-05-22 14:00:00',
            # 'end_date': '2019-05-22 16:00:00',
            # 'jitter': 10

        }

        # {
        #     'id': 'date_trigger',
        #     'func': 'application.config.scheduler:print_test',
        #     'args': ('joke',),
        #     'trigger': 'date',
        #     'run_date': '2019-05-22 11:58:00'
        # }

        # {
        #     'id': 'date_trigger',
        #     'func': 'application.config.scheduler:print_test',
        #     'args': ('joke',),
        #     'trigger': 'date',
        #     'run_date': date(2019, 5, 22)
        # }

        # {
        #     'id': 'date_trigger',
        #     'func': 'application.config.scheduler:print_test',
        #     'args': ('joke',),
        #     'trigger': 'date',
        #     'run_date': datetime(2019, 5, 22, 12, 5, 0, 0)
        # }

        # {
        #     'id': 'cron_trigger',
        #     'func': 'application.config.scheduler:print_test',
        #     'args': ('joke',),
        #     'trigger': 'cron',
        #     'month': '6-8,11-12',
        #     'day': '3rd fri',
        #     'start_date': '2019-05-22 14:00:00',
        #     'end_date': '2019-05-22 16:00:00',
        #     'jitter': 10
        #
        # }

        # {
        #     'id': 'cron_trigger',
        #     'func': 'application.config.scheduler:print_test',
        #     'args': ('joke',),
        #     'trigger': CronTrigger.from_crontab('* * * * *'),
        #     'executor': 'process',
        # }

    ]

    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore(),
        # 'sqlalchemy': SQLAlchemyJobStore(url='sqlite:///test.db'),
        # 'redis': RedisJobStore(host='localhost', port=6379),
        # 'rethinkdb': RethinkDBJobStore(host='localhost', port=28015)
        # 'mongodb': MongoDBJobStore(host='localhost',port=27017)
        # 'zookeeper': ZooKeeperJobStore(hosts='localhost:2181')
    }

    SCHEDULER_EXECUTORS = {
        'default': {
            'type': 'threadpool',
            'max_workers': 20
        },
        'process': {
            'type': 'processpool',
            'max_workers': 10
        }
    }

    # SCHEDULER_ALLOWED_HOSTS = ['localhost']
    SCHEDULER_API_ENABLED = True

    SCHEDULER_AUTH = HTTPBasicAuth()
