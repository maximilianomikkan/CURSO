from behave import *
from page_objects.login_po import Login
from page_objects.administration_po import Administration
from page_objects.projects_po import Projects
from page_objects.home_po import Home
from selenium import webdriver
import time


@when("I delete all projects")
def step_impl(context):
    home_po = Home(context.driver)
    home_po.navigate_to_administration()
    admin_po = Administration(context.driver)
    admin_po.navigate_to_projects()
    admin_po.eliminar_proyectos()


@then("I validate all projects were deleted")
def step_impl(context):
    admin_po = Administration(context.driver)
    texto_esperado = "No data to display"
    assert texto_esperado == admin_po.mensaje_valido(), "------------noooooo funcaaaa----------"