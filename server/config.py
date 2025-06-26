# Step 1 - start with configuration 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" # tells key which database to connect to - a sqlite database called mydatabase.db 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # not tracking all modifications to database 

db = SQLAlchemy(app) # create database instance which gives access to the database we're connecting to - mydatabase.db 

# End of Step 1 