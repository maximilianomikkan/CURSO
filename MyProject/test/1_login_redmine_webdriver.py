import os
from selenium import webdriver

# get the path of chromedriver
#remove the .exe extension on linux or mac platform
chrome_driver_path = "/usr/local/bin/chromedriver"


# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()


# navigate to REDMINE LOGIN  page
# driver.get("http://localhost/redmine/login") - RDF
driver.get("http://192.168.64.2/login")

# get the USERNAME textbox
user_name_we = driver.find_element_by_id("username")
user_name_we.clear()

# get the PASSWORD textbox
password_we = driver.find_element_by_id("password")
password_we.clear()

# enter keywords
user_name_we.send_keys("maximilianomikkan")
password_we.send_keys("abc123")

# submit
btn_login_we = driver.find_element_by_name("login")
btn_login_we.click()


# close the browser window
driver.quit()