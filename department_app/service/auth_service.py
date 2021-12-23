from department_app import login_manager, db
from department_app.models.user_model import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def new_user(email, pass_hash, first_name):
    user = User(email=email, password=pass_hash, first_name=first_name)
    db.session.add(user)
    db.session.commit()


def email_exists(email):
    user = User.query.filter_by(email=email).first()
    return user
