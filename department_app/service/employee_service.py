from department_app import db
from department_app.models.employee_model import Employee
from datetime import datetime, date


def get_all_employees() -> list:
    employees = db.session.query(Employee).all()
    today = date.today()
    for employee in employees:
        born = employee.birth_date
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees


def update_employee(emp_uuid, name, salary, birth_date, department):
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    employee.name = name
    employee.salary = salary
    employee.birth_date = birth_date
    employee.department_uuid = department
    db.session.add(employee)
    db.session.commit()


def add_new_employee(name, salary, birth_date, department):
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
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    db.session.delete(employee)
    db.session.commit()
