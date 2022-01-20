from flask import request
from flask_restful import Resource

from department_app.service.department_service import get_all_departments, add_new_department, \
    update_department, delete_department, get_one_department, update_department_patch
from . import api


class DepartmentListApi(Resource):
    """
    Class for Department Api Resource available on '/api/departments' url
    """

    @staticmethod
    def get():
        """
        Endpoint for getting all departments.
        :return: json response that contains all department entries.
        """
        departments = get_all_departments()
        dep = [department.to_dict() for department in departments]
        return dep

    @staticmethod
    def post():
        """
        Endpoint for adding new department.
        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            dep = request_data['dep']
            if len(dep) > 32:
                return {'error': 'Name too long (max length 32 symbols)'}, 400
            department = add_new_department(dep)
        except KeyError:
            return {'error': 'Wrong Key argument'}, 400
        except TypeError:
            return {'error': 'Missing request body. Request body is required for this method.'}, 400
        return department.to_dict(), 201


class DepartmentApiByID(Resource):
    """
    Class for Department Api Resource available on '/api/departments/<uuid>' url
    """

    @staticmethod
    def get(dep_uuid):
        """
        Endpoint for getting one department by id.
        :return: json response that contains one department entry.
        """
        department = get_one_department(dep_uuid)
        return department.to_dict()

    @staticmethod
    def patch(dep_uuid):
        """
        Endpoint for changing an existing department
        without overwriting unspecified fields with None.
        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            dep = request_data.get('dep', '')

        except AttributeError:
            return {'error': 'Missing request body. Request body is required for this method.'}, 400
        if not dep:
            return {'error': 'Wrong data'}, 400
        if len(dep) > 32:
            return {'error': 'Name too long (max length 32 symbols)'}, 400
        update_department_patch(dep_uuid,
                                dep=dep)
        return get_one_department(dep_uuid).to_dict(), 200

    @staticmethod
    def put(dep_uuid):
        """
        Endpoint for changing an existing department.
        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            dep = request_data['dep']
            if len(dep) > 32:
                return {'error': 'Name too long (max length 32 symbols)'}, 400

            update_department(dep_uuid, dep)
        except KeyError:
            return {'error': 'Wrong parameters.'}, 400
        except TypeError:
            return {'error': 'Missing request body. Request body is required for this method.'}, 400
        return get_one_department(dep_uuid).to_dict(), 200

    @staticmethod
    def delete(dep_uuid):
        """
        Endpoint for deleting a department.
        :return: json response containing the message whether the request was successful or not.
        """
        delete_department(dep_uuid)
        return 'Department has been successfully deleted', 200


api.add_resource(DepartmentListApi, '/departments')
api.add_resource(DepartmentApiByID, '/departments/<dep_uuid>')
