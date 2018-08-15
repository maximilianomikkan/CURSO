from tmsangular.page_objects.base_page_tms_po import BasePage
import random
from selenium.webdriver.common.by import By



class Clients(BasePage):

    def __init__(self, driver):
        super(Clients, self).__init__(driver)
        self.driver = driver

    def create_quick_project(self):
        def aleatorio(opciones):
            opciones = list(opciones)
            while True:
                r = random.choice(opciones)
                opciones.remove(r)
                yield r
        gen = aleatorio("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
        client_name = "Cliente "+ next(gen)

        quick_creation_button = self.driver.find_element_by_xpath("//*[@id='quickcreationbutton']/span")
        quick_creation_button.click()

        quick_client_name_field = self.driver.find_element_by_xpath("/html/body/app-root/div/div/div[2]/div/app-clients/app-client-creation/div[2]/form/div[2]/div/input")
        quick_client_name_field.clear()
        quick_client_name_field.send_keys(client_name)

        quick_save_button = self.driver.find_element_by_xpath("/html/body/app-root/div/div/div[2]/div/app-clients/app-client-creation/div[2]/form/div[3]/div[1]/button")
        quick_save_button.click()


    def commercial(self):
        commercial = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/div/div[1]/app-menu/ul/li[1]/a")
        commercial.click()
        clients = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/div/div[1]/app-menu/ul/li[1]/ul/li[1]/a")
        clients.click()


    def get_successfull_quick_client_label(self):
        successfull_project_we = self.driver.find_element_by_xpath("/div/div/div[2]/p")
        return successfull_project_we.text


    def search_client (self,client_name):
        clients_global_filter = self.driver.find_element_by_xpath("/html/body/app-root/div/div/div[2]/div/app-clients/app-clients-grid/div/input")
        clients_global_filter.click
        clients_global_filter.send_keys(client_name)



    # def create_full_project(self):
    #     ######
    #     full_creation_button = self.driver.find_element_by_xpath("//*[@id='fullcreationbutton']/span")
    #     ######
    #     client_name_field = self.driver.find_element_by_xpath("/html/body/app-root/div/div/div[2]/div/app-clients/app-client-creation/div[2]/form/div[2]/div[1]/input")
    #     industry_field = self.driver.find_element_by_xpath("")
    #     activity_field = self.driver.find_element_by_xpath("")
    #     subsidiary_field = self.driver.find_element_by_xpath("")
    #     currency_field = self.driver.find_element_by_xpath("")
    #     sap_code_field = self.driver.find_element_by_xpath("")
    #     address_field = self.driver.find_element_by_xpath("")
    #     country_field = self.driver.find_element_by_xpath("")
    #     state_field = self.driver.find_element_by_xpath("")
    #     city_field = self.driver.find_element_by_xpath("")
    #     zipcode_field = self.driver.find_element_by_xpath("")
    #     website_field = self.driver.find_element_by_xpath("")
    #     active_field = self.driver.find_element_by_xpath("")
    #     save_button = self.driver.find_element_by_xpath("")
    #     cancel_field = self.driver.find_element_by_xpath("")
    #
    #     #get the NEW_PROJECT link
    #     search_field_menu_new_project = self.driver.find_element_by_xpath("//*[@id='content']/div[1]/a")
    #     search_field_menu_new_project.click()
    #     # verificar si estoy en la otra pagina
    #
    #
    #
    # def complete_new_project_form(self):
    #     def aleatorio(opciones):
    #         opciones = list(opciones)
    #         while True:
    #             r = random.choice(opciones)
    #             opciones.remove(r)
    #             yield r
    #
    #     gen = aleatorio("abcdefghijklmnohghskjfhskfjsdfspqrstuvwxyz")
    #     nombre_de_proyecto = next(gen)
    #     descripcion_de_proyecto = "Descripcion del Proyectoo ", nombre_de_proyecto
    #     identificador_de_proyecto = "identificador-del-proyectoo-", nombre_de_proyecto
    #
    #     # ELEMENTS
    #     search_field_project_name = self.driver.find_element_by_id("project_name")
    #     search_field_project_description = self.driver.find_element_by_id("project_description")
    #     search_field_project_identifier = self.driver.find_element_by_id("project_identifier")
    #     # CLEARS
    #     search_field_project_name.clear()
    #     search_field_project_description.clear()
    #     search_field_project_identifier.clear()
    #     # SENDS
    #     search_field_project_name.send_keys("Proyecto ", nombre_de_proyecto)
    #     search_field_project_description.send_keys(descripcion_de_proyecto)
    #     search_field_project_identifier.send_keys(identificador_de_proyecto)
    #
    #
    #     # Locators de checkboxes en Elementes
    #     search_checkbox_repository = self.driver.find_element_by_id("project_enabled_module_names_repository")
    #     search_field_project_public = self.driver.find_element_by_id("project_is_public")
    #     search_checkbox_boards = self.driver.find_element_by_id("project_enabled_module_names_boards")
    #     search_checkbox_news = self.driver.find_element_by_id("project_enabled_module_names_news")
    #     search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
    #     search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
    #     search_checkbox_documents = self.driver.find_element_by_id("project_enabled_module_names_documents")
    #     search_checkbox_gantt = self.driver.find_element_by_id("project_enabled_module_names_gantt")
    #     search_checkbox_files = self.driver.find_element_by_id("project_enabled_module_names_files")
    #     search_checkbox_wiki = self.driver.find_element_by_id("project_enabled_module_names_wiki")
    #
    #     # enter CHECKBOX PUBLIC keyword
    #     search_field_project_public.click()
    #     search_checkbox_repository.click()
    #     # Foros
    #     search_checkbox_boards.click()
    #     # Noticias
    #     search_checkbox_news.click()
    #     # Calendario
    #     search_checkbox_calendar.click()
    #     # Documentos
    #     search_checkbox_documents.click()
    #     # Gantt
    #     search_checkbox_gantt.click()
    #     # Ficheros
    #     search_checkbox_files.click()
    #     # Wiki
    #     search_checkbox_wiki.click()
    #
    #
    #     # Click on CREATE button
    #     search_create_button = self.driver.find_element_by_name("commit")
    #     search_create_button.click()
    #
    #
    #     # Click on SAVE button
    #     search_save_button = self.driver.find_element_by_name("commit")
    #     search_save_button.click()
    #
    #
    #     print("------------------------------------Proyecto", nombre_de_proyecto,
    #           "creado con Éxito------------------------------------")
    #
    #
    #
    # def navigate_to_projects(self):
    #     search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
    #     # get the PROJECT link                                               //*[@id="top-menu"]/ul/li[3]/a
    #     search_field_menu_projects.click()
    #
    #
    # def get_new_project_label(self):
    #     new_project_we = self.driver.find_element_by_xpath("//*[@id='content']/h2")
    #     return new_project_we.text


