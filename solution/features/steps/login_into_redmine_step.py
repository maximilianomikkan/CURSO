from behave import *
from solution.page_objects.login_po import Login
from solution.page_objects.home_po import Home
from selenium import webdriver


@given("Setup chrome driverq")
def step_impl(context):
    #driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/solution/lfs/webdriver/chromedriver")
    driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/solution/lfs/webdriver/chromedriver.exe")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver


@given("I connect to redmineq")
def step_impl(context):
    #urlMAC = "http://192.168.64.2/login"
    #context.driver.get(urlMAC)

    urlDELL = "http://localhost/redmine/login"
    context.driver.get(urlDELL)


@when("I login into redmineq")
def step_impl(context):
    login_po = Login(context.driver)

    for row in context.table:
        login_po.complete_and_sumbit(user= row["user"], password= row["password"])


@then("Validate I'm logged inq")
def step_impl(context):
    home_po = Home(context.driver)
    texto_esperado = "Logged in as mmikkan"
    #texto_esperado = "Logged in as maximilianomikkan"
    assert texto_esperado == home_po.get_logged_label()
    print("------------------------------------Login realizado con Éxito------------------------------------")
