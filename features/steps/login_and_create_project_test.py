from behave import *
from page_objects.login_po import Login
from page_objects.home_po import Home
from page_objects.projects_po import Projects
from page_objects.my_page_po import MyPage
from page_objects.home_po import Home
from selenium import webdriver


@given("Setup chrome driver")
def step_impl(context):
    driver = webdriver.Chrome(executable_path="/Users/maximacbook/Repositorio1/lfs/webdriver/chromedriver")
    #driver = webdriver.Chrome(executable_path="C:/Users/mmikkan/Repositorio1/lfs/webdriver/chromedriver.exe")

    driver.implicitly_wait(3)
    driver.maximize_window()
    context.driver = driver


@given("I connect to redmine")
def step_impl(context):
    urlMAC = "http://192.168.64.2/login"
    context.driver.get(urlMAC)

    #urlDELL = "http://localhost/redmine/login"
    #context.driver.get(urlDELL)


@when("I login into redmine")
def step_impl(context):
    login_po = Login(context.driver)

    for row in context.table:
        login_po.complete_and_sumbit(user= row["user"], password= row["password"])

    home_po = Home(context.driver)
    # texto_esperado = "Logged in as mmikkan"
    texto_esperado = "Logged in as maximilianomikkan"
    assert texto_esperado == home_po.get_logged_label()



@step("I create a project")
def step_impl(context):
    project_po = Projects(context.driver)
    project_po.navigate_to_projects()

    project_po.navigate_to_new_projects()
    texto_esperado = "New project"
    assert texto_esperado ==project_po.get_new_project_label()
    project_po.complete_new_project_form()


@then("Validate Project was created")
def step_impl(context):
    project_po = Projects(context.driver)
    texto_esperado = "Successful update."
    assert texto_esperado == project_po.get_successfull_project_label(), "------------Houston we've got a problem--3----------"

