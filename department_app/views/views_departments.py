from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import page
from department_app.service import department_service


@page.route('/departments', methods=['POST', 'GET'])
@login_required
def departments_page():
    if request.method == 'POST':
        department_id = request.form['uuid']
        department = request.form['name']
        department_service.update_department(department_id, department)
    return render_template('departments.html', departments=department_service.get_all_departments(), user=current_user)


@page.route('/departments/add/', methods=['GET', 'POST'])
@login_required
def add_department():
    if request.method == 'POST':
        department = request.form['department']
        department_service.add_new_department(department)
        return redirect(url_for('page.departments_page'))
    return render_template('add_department.html', user=current_user)


@page.route('/departments/delete/<dep_uuid>', methods=['POST'])
@login_required
def delete_department(dep_uuid):
    department_service.delete_department(dep_uuid)
    return redirect(url_for('page.departments_page'))
