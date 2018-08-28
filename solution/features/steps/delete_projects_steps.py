from behave import *
from solution.page_objects.login_po import Login
from solution.page_objects.administration_po import Administration
from solution.page_objects.projects_po import Projects
from solution.page_objects.home_po import Home
from selenium import webdriver
import time


@when("I delete all projects")
def step_impl(context):
    home_po = Home(context.driver)
    home_po.navigate_to_administration()

    admin_po = Administration(context.driver)
    admin_po.navigate_to_projects()
    time.sleep(3)
    admin_po.eliminar_proyectos()

@then("I validate all projects were deleted")
def step_impl(context):
    admin_po = Administration(context.driver)
    texto_esperado = "No data to display"
    assert texto_esperado == admin_po.mensaje_valido(), "------------noooooo funcaaaa----------"







    # if valid == "false":
    #     texto_esperado = "Usuario o contraseña inválido."
    #     assert texto_esperado == login_po.mensaje_invalid_login(),"------------Escenario con datos incorrectos----------"
    #     print(valid)
    #     print("")
    #
    # else:
    #     if valid == "true":
    #         home_po = Home(context.driver)
    #         texto_esperado = "My page"
    #         assert texto_esperado == home_po.get_logged_label(), "------------Escenario con datos correctos----------"
    #         print(valid)
    #         print("")

