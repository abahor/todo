from datetime import datetime

from flask import abort, flash
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from markupsafe import Markup
from werkzeug.security import generate_password_hash, check_password_hash

from myproject import db, login


# from myproject import app


# from myproject import wa


# from myproject import ma


@login.user_loader
def load_user(user_id):
    return UsersModel.query.get(user_id)


class UsersModel(db.Model, UserMixin):
    __tablename__ = 'UsersModel'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)

    username = db.Column(db.String(64), nullable=False)

    password = db.Column(db.String(128), nullable=False)

    orders = db.relationship('tasks', backref='author', lazy='dynamic')

    def __init__(self, email, employee_id, mobile, username, password, path):
        self.username = username
        self.email = email

        self.password = generate_password_hash(password)



class tasks (db.Model, UserMixin):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('UsersModel.id'), nullable=False)
    done = db.Column(db.bool, default=False)


    def __init__(self, title, user_id, description):
        self.title = title
        self.description = description

        self.user_id = user_id
