from behave import *
from solution.page_objects.login_po import Login
from solution.page_objects.home_po import Home
from selenium import webdriver
import time


@given("Setup chrome driver")
def step_impl(context):
    driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio/solution/lfs/webdriver/chromedriver")
    #driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio/solution/lfs/webdriver/chromedriver.exe")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver


@given("I connect to redmine")
def step_impl(context):
    urlMAC = "http://192.168.64.2/login"
    context.driver.get(urlMAC)

    #urlDELL = "http://localhost/redmine/login"
    #context.driver.get(urlDELL)


@when("I login as '<valid>' user into redmine with '<user>' and '<password>'")
def step_impl(context, valid, user, password):
    login_po = Login(context.driver)
    time.sleep(4)
    login_po.complete_and_sumbit(user=["user"], password=["password"], valid=["valid"])


@then("Validate I'm logged in")
def step_impl(context):
    home_po = Home(context.driver)
    #texto_esperado = "Logged in as mmikkan"
    texto_esperado = "Logged in as maximilianomikkan"
    assert texto_esperado == home_po.get_logged_label()
    print("------------------------------------Login realizado con Éxito------------------------------------")
