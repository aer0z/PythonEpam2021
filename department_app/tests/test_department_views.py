"""
Tests for department views
"""
import http

from department_app.tests.configtest import BaseTest


class TestDepartmentViews(BaseTest):
    """
    Class for department views test cases.
    """

    def test_departments(self):
        """
        Test '/departments' route
        """
        response = self.app.get('/departments')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_departments_post(self):
        """
        Test '/departments' route for post request
        """
        response = self.app.post('/departments',
                                 data={'uuid': '7330c65a-79d8-11ec-90d6-0242ac120003',
                                       'dep': 'new_department',
                                       },
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_get(self):
        """
        Test '/departments/add/' route
        """
        response = self.app.get('/departments/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_post(self):
        """
        Test '/departments/add/' route for post request
        """
        response = self.app.post('/departments/add/', data={'dep': 'new_department',
                                                            },
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_department(self):
        """
        Test '/departments/delete/<uuid>' route
        """
        response = self.app.post('/departments/delete/7330c65a-79d8-11ec-90d6-0242ac120003',
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
