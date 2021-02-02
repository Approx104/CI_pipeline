from flask import Flask, request
from db_connector import cursor, pymysql
import datetime
import os
import signal


app = Flask(__name__)


# Get user name from DB with user ID
def get_user_name_from_db(user_id):
    cursor.execute('SELECT user_name FROM sys.users WHERE user_id = '"{}"''.format(user_id))
    return cursor.fetchone()


# Check if user exists
def check_user(user_id):
    cursor.execute('SELECT user_name FROM sys.users WHERE user_id = '"{}"''.format(user_id))
    my_result = cursor.fetchall()
    id_to_index = int(user_id) - 1
    get_error = my_result[id_to_index]


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    # GET
    if request.method == 'GET':
        try:
            # Query user name from DB
            cursor.execute('SELECT user_name FROM sys.users WHERE user_id = '"{}"''.format(user_id))
            my_result = get_user_name_from_db(user_id)
            return {'status': 'ok', 'user_name': my_result[0]}, 200  # status code
        except IndexError:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code

    # POST
    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data["user_name"]
            # time
            time = datetime.datetime.now()
            # save user into DB
            loggit = """
                    INSERT INTO sys.users (user_name, user_id, creation_date)
                    VALUES
                        (%s, %s, %s)
                """
            cursor.execute(loggit, (user_name, user_id, time))
            # Return success json
            return {'user id': user_id, 'user name': user_name, 'status': 'ok'}, 200  # status code
        except pymysql.err.IntegrityError:
            # Return error
            return {'reason': 'id already exists', 'status': 'error'}, 500  # status code

    # PUT
    elif request.method == 'PUT':
        try:
            # Check if user exists
            check_user(user_id)
            # getting the json data payload from request
            request_data = request.json
            user_name = request_data["user_name"]
            # updating DB
            cursor.execute("UPDATE sys.users SET user_name = %s WHERE user_id = %s", (user_name, user_id))
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except IndexError:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code

    # DELETE
    elif request.method == 'DELETE':
        try:
            # Check if user exists
            check_user(user_id)
            # updating DB
            cursor.execute('DELETE FROM sys.users WHERE user_id = '"{}"''.format(user_id))
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except IndexError:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
