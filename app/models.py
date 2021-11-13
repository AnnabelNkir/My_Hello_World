from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    _tablename_ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # blog = db.relationship('Blog', backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    # comment = db.relationship('Comment', backref='user', lazy='dynamic')

   

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def _repr_(self):
        return f'User{self.username}'
    
    class Quote:
        """
         Blueprint class for quotes consumed from API
         """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote