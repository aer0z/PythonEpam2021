"""
Module for testing employee model
"""
from department_app import db
from department_app.models.employee_model import Employee
from configtest import BaseTest


class TestEmployee(BaseTest):
    """
    Class for employee model test cases
    """

    def test_employee_model(self):
        """
        Testing if the string representation of
        employee is correct
        """
        employee = Employee(uuid='2',
                            name='Name',
                            salary=15000,
                            birth_date='1987-06-06',
                            department_uuid='7330c65a-79d8-11ec-90d6-0242ac120003')
        db.session.add(employee)
        db.session.commit()
        self.assertEqual('Name', repr(employee))
