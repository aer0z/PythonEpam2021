from department_app import db


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), nullable=False)
