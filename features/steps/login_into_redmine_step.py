from behave import *
from page_objects.login_po import Login
from page_objects.home_po import Home
from page_objects.my_page_po import MyPage
from selenium.webdriver.common.by import By
from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

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

