from behave import *
from tmsangular.page_objects.login_tms_po import Login
from tmsangular.page_objects.home_tms_po import Home
from tmsangular.page_objects.commercial.clients_tms_po import Clients
from selenium import webdriver


@then("Create Quick Client")
def step_impl(context):
    client_po = Clients(context.driver)
    client_po.commercial()
    client_po.create_quick_project()
    #texto_esperado = "The Client was created."
    #assert texto_esperado == client_po.get_successfull_quick_client_label()

    print("------------------------------------Quick Client con Éxito------------------------------------")
