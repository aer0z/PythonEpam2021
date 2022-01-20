"""
Tests for auth service
"""
from department_app import db
from department_app.tests.configtest import BaseTest
from department_app.models.user_model import User
from department_app.service import auth_service


class TestAuthService(BaseTest):
    @staticmethod
    def fill_user_table():
        """
        Fill database with test data.
        """
        user = User(first_name='test_user', email='test_email', password='test_pass')
        db.session.add(user)
        db.session.commit()

    def test_email_exists(self):
        """
        Test if email exists.
        """
        self.fill_user_table()
        self.assertEqual(True, auth_service.email_exists('test_email'))

    def test_not_email_exists(self):
        """
        Test if email don't exist.
        """
        self.fill_user_table()
        self.assertEqual(False, auth_service.email_exists('sddsa'))

    def test_new_user(self):
        """
        Test add new user operation.
        """
        auth_service.new_user('test_user', 'test_email', 'test_pass')
        self.assertEqual(1, User.query.count())
