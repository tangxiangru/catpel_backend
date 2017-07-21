# coding:utf-8

"""
sql models

use: Flask-SQLAlchemy
-- http://flask-sqlalchemy.pocoo.org/2.1/

"""


from flask import current_app,request
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from wtforms.validators import Email
from itsdangerous import JSONWebSignatureSerializer as Serializer

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(164), unique=True, index=True)
    password_hash = db.Column(db.String(164))
    time = db.Column(db.Float)
    forgive_time = db.Column(db.Integer,default=5)
    bind_id = db.Column(db.Integer)
    
    def set_bind_id(self,the_id):
        self.bind_id = the_id

    def settime(self,time):
        self.time=time

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm': self.id})
    
    def generate_auth_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser



