from . import api
import datetime
from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from department_app.service.employee_service import get_all_employees, get_one_employee, \
    update_employee_patch, update_employee, delete_employee, add_new_employee


class EmployeeApiId(Resource):
    @staticmethod
    def get(emp_uuid):
        """
        Endpoint for getting one employee by id.
        :return: json response that contains one employee entry.
        """
        employee = get_one_employee(emp_uuid)
        return employee.to_dict()

    @staticmethod
    def patch(emp_uuid):
        """
        Endpoint for changing an existing employee
        without overwriting unspecified fields with None.
        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            for key in request_data.keys():
                if key not in ['name', 'salary', 'birth_date', 'department_uuid']:
                    return {'error': 'Wrong data'}, 400
        except AttributeError:
            return {'error': 'Missing request body. Request body is required for this method.'}, 400

        name = request_data.get('name')
        salary = request_data.get('salary')
        birth_date = request_data.get('birth_date')
        department_uuid = request_data.get('department_uuid')

        if error := validate(name=name,
                             salary=salary,
                             birth_date=birth_date,
                             department_uuid=department_uuid):
            return error

        try:
            update_employee_patch(emp_uuid=emp_uuid,
                                  name=name,
                                  salary=salary,
                                  birthday=birth_date,
                                  department=department_uuid)
        except IntegrityError:
            return {'error': 'Department with specified ID do not exist'}, 400
        return get_one_employee(emp_uuid).to_dict(), 200

    @staticmethod
    def put(emp_uuid):
        """
        Endpoint for changing an existing employee.
        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            name = request_data['name']
            salary = request_data['salary']
            birth_date = request_data['birth_date']
            department_uuid = request_data['department_uuid']
        except KeyError:
            return {'error': 'Wrong parameters. Note: all parameters (name,'
                             ' salary, date_of_birth,'
                             ' department_id)'
                             ' are required for PUT method.'}, 400
        except TypeError:
            return {'error': 'Missing request body. Request body is required for this method.'}, 400

        if error := validate(name=name,
                             salary=salary,
                             birth_date=birth_date,
                             department_uuid=department_uuid):
            return error
        try:
            update_employee(emp_uuid=emp_uuid,
                            name=name,
                            salary=salary,
                            birth_date=birth_date,
                            department=department_uuid)
        except IntegrityError:
            return {'error': 'Department with specified ID do not exist'}, 400
        return get_one_employee(emp_uuid).to_dict(), 200

    @staticmethod
    def delete(emp_uuid):
        """
        Endpoint for deleting an employee.
        :return: json response containing the message whether the request was successful or not.
        """
        delete_employee(emp_uuid)
        return 'Employee has been successfully deleted', 200


def validate(*, name, salary, birth_date, department_uuid):
    """
    Data validation.
    """
    if name and len(name) > 64:
        return {'error': 'Full name too long (max length 64 symbols)'}, 400
    if salary and not str(salary).isdigit():
        return {'error': 'Wrong data type. Salary must contain only digits'}, 400
    if department_uuid and len(str(department_uuid)) != 36:
        return {'error': 'Wrong data. Department UUID must contain exactly 36 symbols'}, 400
    if birth_date:
        try:
            datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            return {'error': 'Wrong date format. Please use YYYY-MM-DD format'}, 400
    return None


api.add_resource(EmployeeApiId, '/employees/<emp_uuid>')
