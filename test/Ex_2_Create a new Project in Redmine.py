051.
import unittest
from selenium import webdriver
import random


def aleatorio(opciones):
    opciones = list(opciones)
    while True:
        r = random.choice(opciones)
        opciones.remove(r)
        yield r
gen = aleatorio ("abcdefghijklmnopqrstuvwxyz")

nombre_de_proyecto = next(gen)
descripcion_de_proyecto = "Descripcion del Proyecto ",nombre_de_proyecto
identificador_de_proyecto = "identificador-del-proyecto-", nombre_de_proyecto



class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to Redmine Login  page
        self.driver.get("http://192.168.64.2/login/")


    def test_search_by_id(self):
        # get the USERNAME textbox
        self.search_field_username = self.driver.find_element_by_id("username")
        self.search_field_username.clear()

        # get the PASSWORD textbox
        self.search_field_password = self.driver.find_element_by_id("password")
        self.search_field_password.clear()

        # enter USERNAME keyword
        self.search_field_username.send_keys("maximilianomikkan")

        # enter PASSWORD keyword
        self.search_field_password.send_keys("cardaABC123")

        # get the LOGIN button
        self.search_field_login = self.driver.find_element_by_name("login")
        self.search_field_login.click()

        # ASSERT
        self.search_field_user_active = self.driver.find_element_by_xpath("//*[@id='loggedas']/a")
        assert self.search_field_user_active.text == "maximilianomikkan", "------------Houston we've got a problem--1----------"

        # get the PROJECT link
        self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        self.search_field_menu_projects.click()

        # get the NEW_PROJECT link
        self.search_field_menu_new_project = self.driver.find_element_by_xpath("//*[@id='content']/div[1]/a")
        self.search_field_menu_new_project.click()

        # ASSERT
        self.search_field_new_project_tittle = self.driver.find_element_by_xpath("//*[@id='content']/h2")
        assert self.search_field_new_project_tittle.text == "Nuevo proyecto", "------------Houston we've got a problem--2----------"

        # get the NAME textbox
        self.search_field_project_name = self.driver.find_element_by_id("project_name")
        self.search_field_project_name.clear()

        # enter NAME keyword
        self.search_field_project_name.send_keys("Proyecto ",nombre_de_proyecto)

        # get the DESCRIPTION textbox
        self.search_field_project_description = self.driver.find_element_by_id("project_description")
        self.search_field_project_description.clear()

        # enter DESCRIPTION keyword
        self.search_field_project_description.send_keys(descripcion_de_proyecto)

        # get the IDENTIFIER textbox
        self.search_field_project_identifier = self.driver.find_element_by_id("project_identifier")
        self.search_field_project_identifier.clear()

        # enter IDENTIFIER keyword
        self.search_field_project_identifier.send_keys(identificador_de_proyecto)

        # get the CHECKBOX PUBLIC textbox
        self.search_field_project_public = self.driver.find_element_by_id("project_is_public")

        # enter CHECKBOX PUBLIC keyword
        self.search_field_project_public.click()

        # Uncheck some checkboxes
        # Repositorio
        self.search_checkbox_repository = self.driver.find_element_by_id("project_enabled_module_names_repository")
        self.search_checkbox_repository.click()

        # Foros
        self.search_checkbox_boards = self.driver.find_element_by_id("project_enabled_module_names_boards")
        self.search_checkbox_boards.click()

        # Noticias
        self.search_checkbox_news = self.driver.find_element_by_id("project_enabled_module_names_news")
        self.search_checkbox_news.click()

        # Calendario
        self.search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
        self.search_checkbox_calendar.click()

        # Documentos
        self.search_checkbox_documents = self.driver.find_element_by_id("project_enabled_module_names_documents")
        self.search_checkbox_documents.click()

        # Gantt
        self.search_checkbox_gantt = self.driver.find_element_by_id("project_enabled_module_names_gantt")
        self.search_checkbox_gantt.click()

        # Ficheros
        self.search_checkbox_files = self.driver.find_element_by_id("project_enabled_module_names_files")
        self.search_checkbox_files.click()

        # Wiki
        self.search_checkbox_wiki = self.driver.find_element_by_id("project_enabled_module_names_wiki")
        self.search_checkbox_wiki.click()

        # Click on CREATE button
        self.search_create_button = self.driver.find_element_by_xpath("//*[@id='new_project']/input[3]")
        self.search_create_button.click()

        # Click on SAVE button
        self.search_save_button = self.driver.find_element_by_name("commit")
        self.search_save_button.click()

        # ASSERT
        self.search_field_project_was_created = self.driver.find_element_by_id("flash_notice")
        assert self.search_field_project_was_created.text == "Modificación correcta.", "------------Houston we've got a problem--3----------"

        # get the PROJECT link                                                      //*[@id="top-menu"]/ul/li[3]/a
        self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        self.search_field_menu_projects.click()

        print("------------------------------------Proyecto", nombre_de_proyecto, "creado con Éxito------------------------------------")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
