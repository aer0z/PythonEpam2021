"""
Module for logic of pages that starts with /departments
"""

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import page
from department_app.service import department_service


@page.route('/departments', methods=['POST', 'GET'])
@login_required
def departments_page():
    """
    Render departments page
    :return: departments page
    """
    if request.method == 'POST':
        department_id = request.form['uuid']
        dep = request.form['dep']
        department_service.update_department(department_id, dep)
    return render_template('departments.html', departments=department_service.get_all_departments(), user=current_user)


@page.route('/departments/add/', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Page that add department to database
    :return: render page
    """
    if request.method == 'POST':
        dep = request.form['dep']
        department_service.add_new_department(dep)
        return redirect(url_for('page.departments_page'))
    return render_template('add_department.html', user=current_user)


@page.route('/departments/delete/<dep_uuid>', methods=['POST'])
@login_required
def delete_department(dep_uuid):
    """
    Delete department from database
    :param dep_uuid: uuid of department to delete
    :return: redirect to department page
    """
    department_service.delete_department(dep_uuid)
    return redirect(url_for('page.departments_page'))
