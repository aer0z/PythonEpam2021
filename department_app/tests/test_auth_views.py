"""
Tests for auth views
"""
import http

from werkzeug.security import generate_password_hash

from department_app import db
from department_app.tests.configtest import BaseTest
from department_app.models.user_model import User


class TestAuthViews(BaseTest):
    """
    Class for auth views tests.
    """

    def test_index(self):
        """
        Test '/' route
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login(self):
        """
        Test '/login' route
        """
        response = self.app.get('/login')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register(self):
        """
        Test '/sign-up' route
        """
        response = self.app.get('/sign-up')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_logout(self):
        """
        Test '/logout' route.
        """
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post(self):
        """
        Test '/login' route for post request
        """
        user = User(first_name='test', email='email', password=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/login',
                                 data={'first_name': 'test',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post_incorrect(self):
        """
        Test '/login' route for post request with incorrect data.
        """
        response = self.app.post('/login',
                                 data={'username': 'sdfsf',
                                       'password': 'sfsf'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post(self):
        """
        Test '/sign-up' route for post request
        """
        user = User(first_name='test', email='email', password=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/sign-up',
                                 data={'username': 'test',
                                       'email': 'email',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post_incorrect_username(self):
        """
        Test '/sign-up' route for post request with incorrect username.
        """
        user = User(first_name='test', email='email', password=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/sign-up',
                                 data={'username': 'tests',
                                       'email': 'email',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post_incorrect_email(self):
        """
        Test '/sign-up' route for post request with incorrect email.
        """
        user = User(first_name='test', email='email', password=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/sign-up',
                                 data={'username': 'test',
                                       'email': 'email',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

