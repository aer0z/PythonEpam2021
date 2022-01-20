"""
Test for Employees service
"""
from department_app import db
from department_app.tests.configtest import BaseTest
from department_app.models.employee_model import Employee
from department_app.service import employee_service


class TestEmployeeServices(BaseTest):
    """
    Class for employee CRUD operations test cases.
    """

    def test_get_all_employees(self):
        """
        Test get all employees operation
        """
        employee1 = Employee(uuid='2',
                             name='Name',
                             salary=10000,
                             birth_date='1987-06-06',
                             department_uuid='7330c65a-79d8-11ec-90d6-0242ac120003')
        db.session.add(employee1)
        db.session.commit()
        self.assertEqual(2, len(employee_service.get_all_employees()))

    def test_get_one_employee(self):
        """
        Test get one employee operation
        """
        employee = employee_service.get_one_employee('1')
        self.assertEqual('Name', employee.name)

    def test_update_employee(self):
        """
        Test update employee operation
        """
        employee_service.update_employee(1,
                                         'Name',
                                         10000,
                                         '1955-04-27',
                                         '7330c65a-79d8-11ec-90d6-0242ac120003')
        employee = Employee.query.get(1)
        self.assertEqual('Name', employee.name)
        self.assertEqual(10000, employee.salary)
        self.assertEqual('1955-04-27', str(employee.birth_date))
        self.assertEqual('7330c65a-79d8-11ec-90d6-0242ac120003', employee.department_uuid)

    def test_add_new_employee(self):
        """
        Test add employee operation
        """
        employee_service.add_new_employee('Name',
                                          10000,
                                          '1987-06-06',
                                          '7330c65a-79d8-11ec-90d6-0242ac120003')
        self.assertEqual(2, Employee.query.count())

    def test_delete_employee(self):
        """
        Test delete employee operation
        """
        employee_service.delete_employee('1')
        self.assertEqual(0, Employee.query.count())

    def test_update_employee_patch(self):
        """
        Test update patch department operation
        """
        employee_service.update_employee_patch(1, name='Steve')
        employee_service.update_employee_patch(1,
                                               salary=10000,
                                               birthday='1955-04-27',
                                               department='7330c65a-79d8-11ec-90d6-0242ac120003')
        employee = Employee.query.get(1)
        self.assertEqual('Steve', employee.name)
        self.assertEqual(10000, employee.salary)
