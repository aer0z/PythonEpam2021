"""
CRUD operations for Deparment
"""

from sqlalchemy.sql import func
from department_app import db
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


def get_all_departments():
    """
    Information about all Departments in db
    :return: list of departments
    """
    departments = db.session.query(Department).all()
    for department in departments:
        salary = get_average_salary(department.uuid)
        department.average_salary = float(salary) if salary else 0
        department.number_of_employees = get_number_of_employees(department.uuid)
    return departments


def get_one_department(dep_uuid):
    """
    Select data by id form Departments table.
    :param dep_uuid: uuid of department
    :return: department object
    """
    department = Department.query.filter_by(uuid=dep_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    salary = get_average_salary(department.uuid)
    number_of_employees = get_number_of_employees(department.uuid)
    department.average_salary = float(salary) if salary else 0
    department.number_of_employees = number_of_employees
    return department


def add_new_department(name):
    """
    Add new department to db
    :param name: department name
    :return: last department query
    """
    department = Department(dep=name)
    db.session.add(department)
    db.session.commit()
    return db.session.query(Department).order_by(Department.id.desc()).first()


def update_department(department_uuid, dep):
    """
    Change existing entry in department table.
    :param department_uuid: uuid of department
    :param name: department name
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    department.dep = dep
    db.session.add(department)
    db.session.commit()


def delete_department(department_uuid):
    """
    Delete department from db
    :param department_uuid: uuid of department to delete
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    db.session.delete(department)
    db.session.commit()


def get_average_salary(department_uuid):
    """
    Avarage salary of department by uuid
    :param department_uuid: uuid of department to get average salary
    :return: average salary of department
    """
    return db.session.query(func.avg(Employee.salary)).filter_by(
        department_uuid=department_uuid).scalar()


def get_number_of_employees(department_uuid):
    """
    Number of employees of department by uuid
    :param department_uuid: uuid of department to get number of employees
    :return: number of employees
    """
    return db.session.query(Employee).filter_by(department_uuid=department_uuid).count()


def update_department_patch(department_uuid, *, dep=None):
    """
    Change existing department entry in without overwriting unspecified fields with None.
    :param department_uuid: uuid of department
    :param name: department name
    :param description: department description
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    if dep:
        department.dep = dep
    db.session.add(department)
    db.session.commit()
