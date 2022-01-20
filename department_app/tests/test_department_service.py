"""
Tests for department service
"""
from department_app import db
from department_app.tests.configtest import BaseTest
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee
from department_app.service import department_service


class TestDepartmentServices(BaseTest):
    """
    Class for department CRUD operations test cases.
    """

    def test_get_all_departments(self):
        """
        Test get all departments operation
        """
        department = Department(uuid='2', dep='department2', )
        db.session.add(department)
        db.session.commit()
        self.assertEqual(2, len(department_service.get_all_departments()))

    def test_get_one_department(self):
        """
        Test get one department operation
        """
        department1 = department_service.get_one_department('7330c65a-79d8-11ec-90d6-0242ac120003')
        self.assertEqual('Test Department', department1.dep)

    def test_add_department(self):
        """
        Test add department operation
        """
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        """
        Test update department operation
        """
        department_service.update_department('7330c65a-79d8-11ec-90d6-0242ac120003', 'new_department',
                                             )
        department = Department.query.get(1)
        self.assertEqual('new_department', department.dep)

    def test_update_department_patch(self):
        """
        Test update patch department operation
        """
        department_service.update_department_patch('7330c65a-79d8-11ec-90d6-0242ac120003', dep='new_department')
        department = Department.query.get(1)
        self.assertEqual('new_department', department.dep)


    def test_delete_department(self):
        """
        Test delete department operation
        """
        department_service.delete_department('7330c65a-79d8-11ec-90d6-0242ac120003')
        self.assertEqual(0, Department.query.count())

    @staticmethod
    def add_test_to_db():
        """
        Fill database with test data.
        """
        employee1 = Employee(uuid='2',
                             name='Name',
                             salary=10000,
                             birth_date='1987-06-06',
                             department_uuid='7330c65a-79d8-11ec-90d6-0242ac120003')
        db.session.add(employee1)
        db.session.commit()

    def test_get_average_salary(self):
        """
        Test get average salary operation
        """
        self.add_test_to_db()
        self.assertEqual(15000, department_service.get_average_salary('7330c65a-79d8-11ec-90d6-0242ac120003'))

    def test_get_number_of_employees(self):
        """
        Test get number of employees operation
        """
        self.add_test_to_db()
        self.assertEqual(2, department_service.get_number_of_employees('7330c65a-79d8-11ec-90d6-0242ac120003'))
