from behave import *
from solution.page_objects.login_po import Login
from solution.page_objects.projects_po import Projects
from solution.page_objects.home_po import Home
from selenium import webdriver



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

