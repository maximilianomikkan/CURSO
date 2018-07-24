class Home():
    # Top menu locator
    # LEFT
    _lnk_home_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[1]/a")

    _lnk_my_page_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[2]/a")

    _lnk_projects_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[3]/a")

    _lnk_administration_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[4]/a")

    _lnk_help_loc = (By.XPATH, "//*[@id='top-menu']/ul/li[5]/a")

    # RIGHT
    _lnk_user_loc = (By.XPATH, "//*[@id='loggedas']/a")

    _lnk_my_account_loc = (By.XPATH, "//*[@id='account']/ul/li[1]/a")

    _lnK_sign_out_loc = (By.XPATH, "//*[@id='account']/ul/li[2]/a")

    def __init__(self, driver):
        super(Home, self).__init__(driver)



    def click_on_link(self):
        we = self.driver.find_element(self._lnk_home_loc[0], self._lnk_home_loc[1])

