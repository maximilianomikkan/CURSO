from behave import *
from solution.page_objects.login_po import Login
from solution.page_objects.projects_po import Projects
from solution.page_objects.home_po import Home
from selenium import webdriver
import time
from faker import Faker


import requests
import urllib.request
from bs4 import BeautifulSoup


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


@when("I validate I'm logged in '{valid}'")
def step_impl(context, valid):
    login_po = Login(context.driver)
    if valid == "false":
        texto_esperado = "Usuario o contraseña inválido."
        assert texto_esperado == login_po.mensaje_invalid_login(),"------------Escenario con datos incorrectos----------"
    else:
        if valid == "true":
            home_po = Home(context.driver)
            texto_esperado = "My page"
            assert texto_esperado == home_po.get_logged_label(), "------------Escenario con datos correctos----------"