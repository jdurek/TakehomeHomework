# Going to use Flask to create a quick API that exposes some URL endpoints
# These endpoints will then be used as a relay between the frontend and the DB

from flask import Flask, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import MySQLdb.cursors
import ast

app = Flask(__name__)
cors = CORS(app)

# Future TODO - Replace these hardcoded values with Env vars
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'CipherAdmin'
app.config['MYSQL_DB'] = 'Cipher'


mysql = MySQL(app)

@app.route('/api_login', methods=['POST'])
def login():
    msg = ''
    # TODO - figure out why the the JSON body isn't passing/parsing correctly
    # At least .data seems to guarantee a bytes object I can manually parse for now

    if request.method == 'POST':
        print("Correct type passed, checking args...")
    
    # Converting the string passed in by POST
    fmtData = ast.literal_eval(request.data.decode())
    print(fmtData)

    if 'username' in fmtData and 'password' in fmtData:
        # Trigger query to DB, valid string was provided
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from users where password = SHA1(CONCAT(salt, %s)) and email = %s', (fmtData['password'], fmtData['username']))
        account = cursor.fetchone()

        if account == None:
            print("Failed login attempt")
            return jsonify('Failure'), 401
        else:
            # Future TODO - Generate a secure token and return it as part of the response
            return jsonify('Success'), 200
    else:
        # Return generic error
        return jsonify('Failure'), 400

