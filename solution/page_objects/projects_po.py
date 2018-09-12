from solution.page_objects.base_page_po import BasePage
from faker import Faker


class Projects(BasePage):

    def __init__(self, driver):
        super(Projects, self).__init__(driver)
        self.driver = driver


    def navigate_to_new_projects(self):
        #get the NEW_PROJECT link
        search_field_menu_new_project = self.driver.find_element_by_xpath("//*[@id='content']/div[1]/a")
        search_field_menu_new_project.click()
        # verificar si estoy en la otra pagina


    def complete_new_project_form(self):
        faker = Faker()
        name = faker.word().lower()

        # ELEMENTS
        search_field_project_name = self.driver.find_element_by_xpath("//*[@id='project_name']")
        search_field_project_description = self.driver.find_element_by_xpath("//*[@id='project_description']")
        search_field_project_identifier = self.driver.find_element_by_xpath("//*[@id='project_identifier']")

        # CLEARS
        search_field_project_name.clear()
        search_field_project_description.clear()

        # SENDS
        search_field_project_name.send_keys("proyecto_", name)
        search_field_project_description.send_keys("descripcion_", name)

        # CLEARS and SENDS
        search_field_project_identifier.clear()
        search_field_project_identifier.send_keys("identificador_", name)



        # Locators de checkboxes en Elementos W
        search_checkbox_repository = self.driver.find_element_by_id("project_enabled_module_names_repository")
        search_field_project_public = self.driver.find_element_by_id("project_is_public")
        search_checkbox_boards = self.driver.find_element_by_id("project_enabled_module_names_boards")
        search_checkbox_news = self.driver.find_element_by_id("project_enabled_module_names_news")
        search_checkbox_calendar = self.driver.find_element_by_id("project_enabled_module_names_calendar")
        search_checkbox_documents = self.driver.find_element_by_id("project_enabled_module_names_documents")
        search_checkbox_gantt = self.driver.find_element_by_id("project_enabled_module_names_gantt")
        search_checkbox_files = self.driver.find_element_by_id("project_enabled_module_names_files")
        search_checkbox_wiki = self.driver.find_element_by_id("project_enabled_module_names_wiki")

        # enter CHECKBOX PUBLIC keyword
        search_field_project_public.click()
        search_checkbox_repository.click()
        # Foros
        search_checkbox_boards.click()
        # Noticias
        search_checkbox_news.click()
        # Calendario
        search_checkbox_calendar.click()
        # Documentos
        search_checkbox_documents.click()
        # Gantt
        search_checkbox_gantt.click()
        # Ficheros
        search_checkbox_files.click()
        # Wiki
        search_checkbox_wiki.click()


        #screenshot = pyautogui.screenshot()
        #screenshot.save("/Users/maximacbook/Repositorio/solution/screenshots/"+dateString+" - "+name+".png")

        # Click on CREATE button
        search_create_button = self.driver.find_element_by_name("commit")
        search_create_button.click()


        # Click on SAVE button
        search_save_button = self.driver.find_element_by_name("commit")
        search_save_button.click()

        # -------------------------
        #screenshot.show()
        # -------------------------

        print("------------------------------------Proyecto", name,
              "creado con Éxito------------------------------------")



    def navigate_to_projects(self):
        search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        # get the PROJECT link                                               //*[@id="top-menu"]/ul/li[3]/a
        search_field_menu_projects.click()


    def get_new_project_label(self):
        new_project_we = self.driver.find_element_by_xpath("//*[@id='content']/h2")
        return new_project_we.text

    def get_successfull_project_label(self):
        successfull_project_we = self.driver.find_element_by_id("flash_notice")
        return successfull_project_we.text

    def navigate_to_administration(self):
        # get the ADMINISTRATION link
        search_field_menu_administration = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[4]/a")
        search_field_menu_administration.click()









