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
    time.sleep(1)
    #login_po.complete_and_sumbit(user=user, password=password)
    login_po.complete_and_sumbit(user, password)
    time.sleep(1)


@Then("I validate I'm logged in '{valid}'")
def step_impl(context, valid):
    login_po = Login(context.driver)
    texto_flash = "Usuario o contraseña inválido."
    if texto_flash == login_po.inicia_sesion():
        print("------------------------------------Login NOOOO realizado con Éxito------------------------------------")
    else:
        print("------------------------------------Login realizado con Éxito------------------------------------")



