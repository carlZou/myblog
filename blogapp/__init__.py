import redis as redis
from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from config import Config

pool = redis.ConnectionPool(host='202.182.105.20', port=6379, password='sa123456', decode_responses=True)
r = redis.Redis(connection_pool=pool)

db = SQLAlchemy()
migrate = Migrate()
session = Session()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)
session.init_app(app)

from blogapp.models import user, posts
from blogapp.routes import auth, user
