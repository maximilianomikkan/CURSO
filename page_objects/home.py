from selenium.webdriver.common.by import By

class Home():


    def __init__(self, driver):
        super(Home, self).__init__(driver)



    def click_on_link(self):
        we = self.driver.find_element(self._lnk_home_loc[0], self._lnk_home_loc[1])

