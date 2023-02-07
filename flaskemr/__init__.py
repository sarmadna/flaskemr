from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "fjasdfj309wef093qkjeflj03qjqdkfjksaf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinic.db"
db = SQLAlchemy(app)

from flaskemr import routes