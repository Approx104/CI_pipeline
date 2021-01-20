from flask import Flask
import requests

app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>')
def user(user_id):
    try:
        # Get user from rest app using API
        res = requests.get("http://127.0.0.1:5000/users/{}".format(user_id))
        data = res.json()
        my_result = str(data['user_name'])
        return "<H1 id='user'>" + my_result + "</H1>"
    except KeyError:
        return "<H1 id='error'>"'no such user:' + user_id + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)
