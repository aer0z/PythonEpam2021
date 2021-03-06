"""
Module for logic of pages that starts with /employees
"""

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from department_app.service import employee_service
from department_app.service.department_service import get_all_departments
from . import page


@page.route('/employees/', defaults={'dep_uuid': None}, methods=['GET', 'POST'])
@page.route('/employees/<dep_uuid>', methods=['GET', 'POST'])
@login_required
def employees(dep_uuid):
    """
    Render employees page
    :param dep_uuid: uuid of department to get it's employees
    :return: employees page
    """
    if request.method == 'POST':
        uuid = request.form['uuid']
        name = request.form['name']
        birth_date = request.form['birth_date']
        salary = request.form['salary']
        dep = request.form['dep']
        employee_service.update_employee(emp_uuid=uuid,
                                         name=name,
                                         salary=salary,
                                         birth_date=birth_date,
                                         dep=dep)
    deps = get_all_departments()
    employees_list = employee_service.get_all_employees()
    return render_template('employees.html', employees=employees_list, departments=deps, user=current_user)


@page.route('/employees/add/', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Page that add employee to db
    :return: render page
    """
    if request.method == 'POST':
        name = request.form['name']
        salary = request.form['salary']
        department = request.form['department']
        birth_date = request.form['birth_date']
        employee_service.add_new_employee(name, salary, birth_date, department)
        return redirect(url_for('page.employees'))
    departments = get_all_departments()
    return render_template('add_employee.html', departments=departments, user=current_user)


@page.route('/employees/delete/<emp_uuid>', methods=['POST'])
@login_required
def delete_employee(emp_uuid):
    """
    Delete department from db
    :param emp_uuid: uuid of employee to delete
    :return: redirect to employees page
    """
    employee_service.delete_employee(emp_uuid)
    return redirect(url_for('page.employees'))
