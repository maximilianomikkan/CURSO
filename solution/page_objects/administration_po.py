from solution.page_objects.base_page_po import BasePage
import time




class Administration(BasePage):
    def __init__(self, driver):
        super(Administration, self).__init__(driver)
        self.driver = driver

    def navigate_to_projects(self):
        # get the projects link
        search_field_menu_administration = self.driver.find_element_by_xpath("//*[@id='admin-menu']/ul/li[1]/a")
        search_field_menu_administration.click()

    def eliminar_proyectos(self):

        while (True):
            try:
                fila = self.driver.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[1]/td[4]/a[3]")
                fila.click()
                yes_checkbutton = self.driver.find_element_by_xpath("//*[@id='confirm']")
                yes_checkbutton.click()

                delete_button = self.driver.find_element_by_xpath("//*[@id='content']/form/p/input")
                delete_button.click()


                if self.driver.find_element_by_xpath("//*[@id='content']/div[2]/table/tbody/tr[1]/td[4]/a[3]"):
                    print("")
                else:
                    return False
            except:
                return False

    def mensaje_valido(self):
        texto_flash = self.driver.find_element_by_xpath("//*[@id='content']/p")

        return texto_flash.text




