'''
Config Tests
'''

import unittest

from department_app.models.department_model import Department
from department_app.models.employee_model import Employee
from department_app import app, db
from department_app.dbcreate import dbname, dbport, dbpass, dbhost, dbuser


class BaseTest(unittest.TestCase):
    """
    Base test case class.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        """
        department = Department(uuid='7330c65a-79d8-11ec-90d6-0242ac120003',
                                dep='Test Department'
                                )
        db.session.add(department)
        db.session.commit()
        employee = Employee(uuid='1',
                            name='Name',
                            salary=20000,
                            birth_date='1987-06-06',
                            department_uuid='7330c65a-79d8-11ec-90d6-0242ac120003')
        db.session.add(employee)
        db.session.commit()

    def setUp(self):
        """
        Setup test client and database before every test case.
        :return:
        """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['LOGIN_DISABLED'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = \
            f'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}:{dbport}/db_test'
        self.app = app.test_client()
        db.create_all()
        self.fill_db()

    def tearDown(self):
        """
        Teardown database after every test case.
        """
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
