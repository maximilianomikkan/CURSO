from behave import fixture, use_fixture
from selenium import webdriver



def before_all(context):
    # create a new Chrome session
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

    # navigate to Redmine Login  page
    # MACBOOK
    # context.driver.get("http://192.168.64.2/login")
    # DELL BSF
    context.driver.get("http://localhost/redmine/login")


def after_all(context):
    # close the browser window
    context.driver.quit()