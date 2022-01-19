"""
CRUD operations for Employee
"""

from department_app import db
from department_app.models.employee_model import Employee
from datetime import datetime, date


def get_all_employees():
    """
    Function that get all employees from db and calculate their age
    :return: list of employees
    """
    employees = db.session.query(Employee).all()
    today = date.today()
    for employee in employees:
        born = employee.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees


def get_one_employee(emp_uuid):
    """""
    Select one employee from database by id and calculate age.
    :param emp_uuid: uuid of employee
    :return: employee object
    """""
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    today = date.today()
    born = employee.birth_date
    employee.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return employee


def update_employee(emp_uuid, name, salary, birth_date, department):
    """
     Change existing employee entry.
    :param emp_uuid: uuid of employee
    :param name: name of employee
    :param salary: salary of employee
    :param birth_date: birthday of employee
    :param department: uuid of employees department
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    employee.name = name
    employee.salary = salary
    employee.birth_date = birth_date
    employee.department_uuid = department
    db.session.add(employee)
    db.session.commit()


def add_new_employee(name, salary, birth_date, department):
    """
    Add new employee to db
    :param name: name of employee
    :param salary: salary of employee
    :param birth_date: birthday of employee
    :param department: uuid of employees department
    """
    employee = Employee(name=name,
                        salary=salary,
                        birth_date=birth_date,
                        department_uuid=department)
    db.session.add(employee)
    db.session.commit()

    emp = db.session.query(Employee).order_by(Employee.id.desc()).first()
    today = date.today()
    born = emp.birth_date
    emp.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return emp


def get_employee_with_params(*, dep_uuid=None, first_date=None, second_date=None):
    """
       Get employees born on a certain date or in the period between dates.
       :param dep_uuid: id of department
       :param first_date: date in format yyyy-mm-dd
       :param second_date: date in format yyyy-mm-dd
       :return: list pf employees
       """
    today = date.today()
    if first_date:
        first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
        if second_date:
            second_date = datetime.strptime(second_date, "%Y-%m-%d").date()
            if dep_uuid:
                employees = Employee.query.filter(
                    Employee.birth_date.between(first_date, second_date)).filter_by(
                    department_uuid=dep_uuid).all()
            else:
                employees = Employee.query.filter(
                    Employee.birth_date.between(first_date, second_date)).all()
        else:
            if dep_uuid:
                employees = Employee.query.filter_by(
                    birth_date=first_date).filter_by(department_uuid=dep_uuid).all()
            else:
                employees = Employee.query.filter_by(birth_date=first_date).all()
    else:
        if dep_uuid:
            employees = Employee.query.filter_by(department_uuid=dep_uuid).all()
        else:
            employees = Employee.query.all()
    for employee in employees:
        born = employee.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees


def delete_employee(emp_uuid):
    """
    Delete employye from db
    :param emp_uuid: uuid of employee to delete
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    db.session.delete(employee)
    db.session.commit()


def update_employee_patch(emp_uuid, *, name=None, salary=None, birthday=None, department=None):
    """
    Change existing employee entry without overwriting unspecified fields with None.
    :param emp_uuid: uuid of employee
    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param department: uuid of employee's department
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    if name:
        employee.name = name
    if salary:
        employee.salary = salary
    if birthday:
        employee.birth_date = birthday
    if department:
        employee.department_uuid = department
    db.session.add(employee)
    db.session.commit()
