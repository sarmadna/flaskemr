#import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app.config['SECRET_KEY'] = "fjasdfj309wef093qkjeflj03qjqdkfjksaf"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'clinic.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flaskemr import routes
