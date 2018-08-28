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


@when("I login as user into redmine with '{user}' and '{password}'")
def step_impl(context, user, password):
    login_po = Login(context.driver)
    #time.sleep(1)
    #login_po.complete_and_sumbit(user=user, password=password)
    login_po.complete_and_sumbit(user, password)
    time.sleep(0.5)


@then("I validate I'm logged in '{valid}'")
def step_impl(context, valid):
    login_po = Login(context.driver)
    if valid == "false":
        texto_esperado = "Usuario o contraseña inválido."
        assert texto_esperado == login_po.mensaje_invalid_login(),"------------Escenario con datos incorrectos----------"
        print(valid)
        print("")

    else:
        if valid == "true":
            home_po = Home(context.driver)
            texto_esperado = "My page"
            assert texto_esperado == home_po.get_logged_label(), "------------Escenario con datos correctos----------"
            print(valid)
            print("")








