"""
Module for testing department model
"""

from configtest import BaseTest
from department_app import db
from department_app.models.department_model import Department


class TestDepartment(BaseTest):
    """
    Class for testing department model
    """

    def test_department_model(self):
        """
        Testing if the string representation of
        department is correct
        """
        department = Department(uuid="2", dep='test_department', )
        db.session.add(department)
        db.session.commit()
        self.assertEqual('test_department', repr(department))
