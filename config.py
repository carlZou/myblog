import os

import redis

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sa123456@202.182.105.20:3307/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'
    # 如果设置为True，则关闭浏览器session就失效。
    # SESSION_PERMANENT = False
    # 是否对发送到浏览器上session的cookie值进行加密
    # SESSION_USE_SIGNER = False
    # 保存到session中的值的前缀
    # SESSION_KEY_PREFIX = 'session'

    SESSION_REDIS = redis.Redis(host='202.182.105.20', port=6379, password='sa123456', decode_responses=False)
