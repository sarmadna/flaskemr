from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "fjasdfj309wef093qkjeflj03qjqdkfjksaf"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/clinic"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flaskemr import routes