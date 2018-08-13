from behave import *
from page_objects.login_po import Login
from page_objects.home_po import Home
from page_objects.my_page_po import MyPage
from page_objects.home_po import Home
from selenium import webdriver


@given("Setup chrome driver")
def step_impl(context):
    # driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/lfs/webdriver/chromedriver")
    driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/lfs/webdriver/chromedriver.exe")

    # if driver == "chrome":
    #     driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/lfs/webdriver/chromedriver")
    #     driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/lfs/webdriver/chromedriver.exe")
    # elif driver == "firefox":\
    #     driver = webdriver.Firefox(executable_path="project_roo/lfs/webdriver/geckodriver")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver


@given("I connect to redmine")
def step_impl(context):
    #urlMAC = "http://192.168.64.2/login"
    #context.driver.get(urlMAC)
    urlDELL = "http://localhost/redmine/login"
    context.driver.get(urlDELL)


@when("I login into redmine")
def step_impl(context):
    login_po = Login(context.driver)
    login_po.complete_and_sumbit("mmikkan","cardaABC123")
    #login_po.complete_and_sumbit("maximilianomikkan", "cardaABC123")


@then("Validate I'm logged in")
def step_impl(context):
    home_po = Home(context.driver)
    texto_esperado = "Logged in as mmikkan"
    #texto_esperado = "Logged in as maximilianomikkan"
    assert texto_esperado == home_po.get_logged_label()