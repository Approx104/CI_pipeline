import requests
import selenium
from selenium import webdriver

try:
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
except selenium.exceptions.WebDriverException:
    raise Exception("Can't find chrome driver!")

# Get user name and user id
get_user_id = input("Enter the users ID: ")
get_user_name = input("Enter the users name: ")
# POST the data
json_data = {"user_name": get_user_name}
new_user = requests.post("http://127.0.0.1:5000/users/{}".format(get_user_id), json=json_data)
# Check if all ok
if new_user.status_code == 500:
    raise Exception("Test failed!")

# GET user and Check if user name matches and response code is good
get_user = requests.get("http://127.0.0.1:5000/users/{}".format(get_user_id))
data = get_user.json()
my_result = data['user_name']
# Check if all ok
if (my_result != json_data['user_name']) or (get_user.status_code != 200):
    raise Exception("Test failed!")
#
# # Check if data was stored using pymysql
# try:
#     cursor.execute('SELECT user_name FROM 7n3ZZQTFqz.users WHERE user_id = '"{}"''.format(get_user_id))
#     my_result = cursor.fetchall()
#     id_to_index = int(get_user_id) - 1
#     get_error = my_result[id_to_index]
# except IndexError:
#     raise Exception("Test failed!")

# Check user name with selenium
driver.get("http://127.0.0.1:5001/users/get_user_data/{}".format(get_user_id))
user_name = driver.find_element_by_id('user')
if user_name.text != get_user_name:
    raise Exception("Test failed!")
