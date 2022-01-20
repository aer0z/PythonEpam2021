from department_app import db
from uuid import uuid4


class Department(db.Model):
    """
       Department model for db.
    """
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(length=36), unique=True, nullable=False, default=uuid4)
    dep = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields
        :return: the department in json format
        """
        try:
            average_salary = self.average_salary
            number_of_employees = self.number_of_employees
        except AttributeError:
            return {'uuid': self.uuid,
                    'dep': self.dep,

                    }
        return {
            'uuid': self.uuid,
            'dep': self.dep,
            'average_salary': average_salary,
            'number_of_employees': number_of_employees
        }

    def __repr__(self):
        return str(self.dep)
