from flask import render_template
from flask_login import login_required, current_user
from . import page


@page.route('/employees/', defaults={'ids': None}, methods=['GET', 'POST'])
@page.route('/employees/<ids>', methods=['GET', 'POST'])
@login_required
def employees(ids):
    return render_template('employees.html', user=current_user)
