from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver




class Home(BasePage):

    def __init__(self, driver):
        #self.driver = driver
        #super(Home, self).__init__(driver)

        # Home locators
        self.txf_home_loc = driver.find_element(By.XPATH, "//*[@id='content']/h2")








# #y además puso esto el Cris
#
#     def __init__(self, driver):
#         super(Home, self).__init__(driver)
#
#
#
#     def click_on_link(self):
#         we = self.driver.find_element(self._lnk_home_loc[0], self._lnk_home_loc[1])

