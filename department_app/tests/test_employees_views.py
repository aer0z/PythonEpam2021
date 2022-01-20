"""
Tests for employees views
"""
import http

from department_app import db
from department_app.tests.configtest import BaseTest
from department_app.models.department_model import Department


class TestEmployeeViews(BaseTest):
    """
    Class for employees views test cases.
    """

    def test_employees(self):
        """
        Test '/employees/' route
        """
        response = self.app.get('/employees/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employees_with_params(self):
        """
        Test '/employees/<uuid>' route
        """
        response = self.app.get('/employees/7330c65a-79d8-11ec-90d6-0242ac120003')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)


    def test_add_employee(self):
        """
        Test '/employees/add/' route
        """
        response = self.app.get('/employees/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_employee_post(self):
        """
        Test '/employees/add/' route for post request
        """
        department = Department(uuid='3', dep='department1')
        db.session.add(department)
        db.session.commit()
        response = self.app.post('/employees/add/',
                                 data={'name': 'test name',
                                       'salary': 2000,
                                       'birth_date': '1975-05-23',
                                       'department': '7330c65a-79d8-11ec-90d6-0242ac120003'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_employee(self):
        """
        Test '/employees/delete/<uuid>' route
        """
        response = self.app.post('/employees/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
