from flask import Flask
from department_app.dbcreate import dbuser, dbname, dbhost, dbpass, SECRET_KEY, dbport
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
conn = f'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'

app.config["SQLALCHEMY_DATABASE_URI"] = conn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from department_app.views import page

app.register_blueprint(page, url_prefix='/')
