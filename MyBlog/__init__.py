from flask import Flask
from flask_mysqldb import MySQL

#Creates the app
app = Flask(__name__)

#Load configurations from the class "configure"
app.config.from_object("db_conn.DevelopmentConfig")
#Initialize and link the app with db
mysqldb = MySQL(app)

