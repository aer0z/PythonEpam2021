from department_app import db
from department_app.models.department_model import Department
from uuid import uuid4


class Employee(db.Model):
    """
    Employee model for db.
    """
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(length=36), unique=True, nullable=False, default=uuid4)
    name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    department_uuid = db.Column(db.String(length=36), db.ForeignKey('department.uuid'))
    department = db.relationship(Department, backref='employee')
