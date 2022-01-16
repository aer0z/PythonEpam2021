from department_app import db
from uuid import uuid4


class Department(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(length=36), unique=True, nullable=False, default=uuid4)
    department = db.Column(db.String(50), nullable=False)
