from flask_login import UserMixin
from department_app import db


class User(UserMixin, db.Model):
    """
        Employee model for db.
    """
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(256))
    first_name = db.Column(db.String(50))
