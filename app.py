from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)