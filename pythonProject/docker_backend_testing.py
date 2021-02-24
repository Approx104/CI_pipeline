import requests
from db_connector import cursor


def test_back(user_id, user_name):
    # POST a new user to API
    json_data = {"user_name": user_name}
    new_user = requests.post("http://127.0.0.1:5000/users/{}".format(user_id), json=json_data)
    if new_user.status_code == 500:
        return False

    # GET user
    get_user = requests.get("http://127.0.0.1:5000/users/{}".format(user_id))
    data = get_user.json()
    my_result = data['user_name']
    # Check if user name matches and response code is good
    if (my_result != json_data['user_name']) or (get_user.status_code != 200):
        return False

    # Query for user
    try:
        cursor.execute('SELECT user_name FROM sys.users WHERE user_id = '"{}"''.format(user_id))
        my_result = cursor.fetchall()
        get_error = my_result[0]
    except IndexError:
        return False

    return True


if test_back(2, 'Boris'):
    print("TEST: Pass")
