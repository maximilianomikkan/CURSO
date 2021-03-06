from page_objects.base_page_po import BasePage


class Home(BasePage):
    def __init__(self, driver):
        super(Home, self).__init__(driver)


    def get_logged_label(self):
        logged_as_we = self.driver.find_element_by_xpath("//*[@id='content']/h2")
        #logged_as_we = self.driver.find_element_by_xpath("//*[@id='loggedas']")
        return logged_as_we.text

    def navigate_to_administration(self):
        # get the administration link
        search_field_menu_administration = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[4]/a")
        search_field_menu_administration.click()





    # def navigate_to_projects(self):
    #     self.search_field_menu_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
    #     self.search_field_menu_projects.click()