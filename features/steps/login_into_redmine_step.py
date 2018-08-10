from behave import *
from page_objects.login_po import Login
from page_objects.home_po import Home
from page_objects.my_page_po import MyPage
from selenium import webdriver


@given('completo el formulario')
def step_impl(context):
    print("---test_login_redmine---")
    login_page = Login(context.driver)
    login_page.complete_and_sumbit("mmikkan", "cardaABC123")


@When('le doy click al boton')
def step_impl(context):
    login_page = Login(context.driver)
    # MACBOOK
    #login_page.complete_and_sumbit("maximilianomikkan", "cardaABC123")
    #DELL BSF
    #login_page.sumbit()
    login_page.btn_submit_loc.click()


@Then('veo el home')
def step_impl(context):
    my_page = MyPage(context.driver)
    assert my_page.lbl2.text == "My page", "------------Houston we've got a problem--2----------"


@given("Setup {driver} driver")
def step_impl(context, driver):
    """
    :type context: behave.runner.Context
    """
    if driver == "chrome":
        driver == webdriver.Chrome(executable_path="project_roo/lfs/webdriver/chromedriver.exe")
    elif driver == "firefox":
        driver = webdriver.Firefox(executable_path="project_roo/lfs/webdriver/geckodriver.exe")


    driver.implicitly_wait(5)
    driver.maximize_window()
    context.driver = driver


@step("I connect to redmine")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = ""
    context.driver.get(url)


@when("I login into redmine")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login_po = Login(context.driver)
    login_po.login("user", "password")


@then("Validate I'm logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected = "Logged in as user"

    assert expected == context.homepage_po.get_logged_as_label()
