import selenium
from selenium import webdriver


try:
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
except selenium.exceptions.WebDriverException:
    raise Exception("Can't find chrome driver!")

driver.get("http://127.0.0.1:5001/users/get_user_data/1")
user_name = driver.find_element_by_id('user')
print(user_name.text)
