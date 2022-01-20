"""
Module for testing user model
"""
from department_app import db
from department_app.models.user_model import User
from department_app.tests.configtest import BaseTest


class TestUser(BaseTest):
    """
    Class for testing user model
    """

    def test_user_model(self):
        """
        Testing if the string representation of
        user is correct
        """
        user = User(email='test_email', password='test_pass', first_name='test_name')
        db.session.add(user)
        db.session.commit()
        self.assertEqual('test_name', repr(user))
