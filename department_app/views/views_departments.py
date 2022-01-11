from flask import render_template
from flask_login import login_required, current_user
from . import page


@page.route('/departments', methods=['POST', 'GET'])
@login_required
def departments_page():
    return render_template('departments.html', user=current_user)
