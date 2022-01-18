"""
Start app
"""
from department_app import db, app

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
    db.init_app(app)
