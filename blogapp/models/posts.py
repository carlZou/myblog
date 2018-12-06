from datetime import datetime

from blogapp import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    post_body = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    yn = db.Column(db.SmallInteger, default=1)

    def __repr__(self):
        "<post: {}>".format(self.title)
