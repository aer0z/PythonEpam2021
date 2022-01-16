from sqlalchemy.sql import func
from department_app import db
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


def get_all_departments():
    departments = db.session.query(Department).all()
    for department in departments:
        salary = get_average_salary(department.uuid)
        department.average_salary = float(salary) if salary else 0
        department.number_of_employees = get_number_of_employees(department.uuid)
    return departments


def add_new_department(name):
    department = Department(department=name)
    db.session.add(department)
    db.session.commit()
    return db.session.query(Department).order_by(Department.id.desc()).first()


def update_department(department_uuid, name):
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    department.name = name
    db.session.add(department)
    db.session.commit()


def delete_department(department_uuid):
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    db.session.delete(department)
    db.session.commit()


def get_average_salary(department_uuid):
    return db.session.query(func.avg(Employee.salary)).filter_by(
        department_uuid=department_uuid).scalar()


def get_number_of_employees(department_uuid):
    return db.session.query(Employee).filter_by(department_uuid=department_uuid).count()
