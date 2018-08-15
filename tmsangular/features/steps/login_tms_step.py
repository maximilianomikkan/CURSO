from behave import *
from tmsangular.page_objects.home_tms_po import Home
from tmsangular.page_objects.login_tms_po import Login
from selenium import webdriver

@given("Setup chrome driverq")
def step_impl(context):
    #driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/solution/lfs/webdriver/chromedriver")
    driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/tmsangular/lfs/webdriver/chromedriver.exe")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver


@given("I connect to tmsangularq")
def step_impl(context):

    url = "http://192.168.7.236/login"
    context.driver.get(url)


@when("I login into tmsangularq")
def step_impl(context):
    login_po = Login(context.driver)

    for row in context.table:
        login_po.complete_and_sumbit(user= row["user"], password= row["password"])


@step("Validate I'm logged inq")
def step_impl(context):
    home_po = Home(context.driver)
    texto_esperado = "Welcome!"
    assert texto_esperado == home_po.get_logged_label()
    print("------------------------------------Login en TMS Angular realizado con Éxito------------------------------------")



@Given("I logged in TMS")
def step_impl(context):
    # driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/solution/lfs/webdriver/chromedriver")
    driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/tmsangular/lfs/webdriver/chromedriver.exe")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver

    url = "http://192.168.7.236/login"
    context.driver.get(url)

    login_po = Login(context.driver)
    for row in context.table:
        login_po.complete_and_sumbit(user= row["user"], password= row["password"])

    home_po = Home(context.driver)
    texto_esperado = "Welcome!"
    assert texto_esperado == home_po.get_logged_label()
    print(
        "------------------------------------Login en TMS Angular realizado con Éxito------------------------------------")



