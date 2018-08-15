from tmsangular.page_objects.base_page_tms_po import BasePage


class Home(BasePage):
    def __init__(self, driver):
        super(Home, self).__init__(driver)


    def get_logged_label(self):
        logged_as_we = self.driver.find_element_by_xpath("/html/body/app-root/div/div/div[2]/div/app-home/div/div/div/div[1]/h1")
        return logged_as_we.text


    # def navigate_to_projects(self):
    #     self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
    #     self.search_field_menu_projects.click()