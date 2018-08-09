import time

from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By
import random



class Projects(BasePage):

    def __init__(self, driver):
        self.driver = driver


    def navigate_to_new_projects(self):
        #get the NEW_PROJECT link
        self.search_field_menu_new_project = self.driver.find_element_by_xpath("//*[@id='content']/div[1]/a")
        self.search_field_menu_new_project.click()
        # verificar si estoy en la otra pagina

        self.search_field_new_project_tittle = self.driver.find_element_by_xpath("//*[@id='content']/h2")


    def complete_new_project_form(self):
        def aleatorio(opciones):
            opciones = list(opciones)
            while True:
                r = random.choice(opciones)
                opciones.remove(r)
                yield r

        gen = aleatorio("abcdefghijklmnohghskjfhskfjsdfspqrstuvwxyz")
        nombre_de_proyecto = next(gen)
        descripcion_de_proyecto = "Descripcion del Proyecto ", nombre_de_proyecto
        identificador_de_proyecto = "identificador-del-proyecto-", nombre_de_proyecto

        # ELEMENTS
        self.search_field_project_name = self.driver.find_element_by_id("project_name")
        self.search_field_project_description = self.driver.find_element_by_id("project_description")
        self.search_field_project_identifier = self.driver.find_element_by_id("project_identifier")
        # CLEARS
        self.search_field_project_name.clear()
        self.search_field_project_description.clear()
        self.search_field_project_identifier.clear()
        # SENDS
        self.search_field_project_name.send_keys("Proyecto ", nombre_de_proyecto)
        self.search_field_project_description.send_keys(descripcion_de_proyecto)
        self.search_field_project_identifier.send_keys(identificador_de_proyecto)


        # Locators de checkboxes en Elementes
        self.search_checkbox_repository = self.driver.find_element_by_id("project_enabled_module_names_repository")
        self.search_field_project_public = self.driver.find_element_by_id("project_is_public")
        self.search_checkbox_boards = self.driver.find_element_by_id("project_enabled_module_names_boards")
        self.search_checkbox_news = self.driver.find_element_by_id("project_enabled_module_names_news")
        self.search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
        self.search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
        self.search_checkbox_documents = self.driver.find_element_by_id("project_enabled_module_names_documents")
        self.search_checkbox_gantt = self.driver.find_element_by_id("project_enabled_module_names_gantt")
        self.search_checkbox_files = self.driver.find_element_by_id("project_enabled_module_names_files")
        self.search_checkbox_wiki = self.driver.find_element_by_id("project_enabled_module_names_wiki")

        # enter CHECKBOX PUBLIC keyword
        self.search_field_project_public.click()
        self.search_checkbox_repository.click()
        # Foros
        self.search_checkbox_boards.click()
        # Noticias
        self.search_checkbox_news.click()
        # Calendario
        self.search_checkbox_calendar.click()
        # Documentos
        self.search_checkbox_documents.click()
        # Gantt
        self.search_checkbox_gantt.click()
        # Ficheros
        self.search_checkbox_files.click()
        # Wiki
        self.search_checkbox_wiki.click()


        # Click on CREATE button
        self.search_create_button = self.driver.find_element_by_name("commit")
        self.search_create_button.click()


        # Click on SAVE button
        self.search_save_button = self.driver.find_element_by_name("commit")
        self.search_save_button.click()


        # ASSERT
        self.search_field_project_was_created = self.driver.find_element_by_id("flash_notice")

        print("------------------------------------Proyecto", nombre_de_proyecto,
              "creado con Éxito------------------------------------")


    def navigate_to_projects(self):
        self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        # get the PROJECT link                                               //*[@id="top-menu"]/ul/li[3]/a
        self.search_field_menu_projects.click()
        time.sleep(2)


