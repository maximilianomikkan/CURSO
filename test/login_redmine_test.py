from page_objects.login_po import Login
from page_objects.home_po import Home
from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By
import time
import unittest

class myTests(BasePage):

    def test_login_redmine(self):
        print("---test_login_redmine---")
        login_page = Login(self.driver)

        # MACBOOK
        #login_page.complete_and_sumbit("maximilianomikkan", "cardaABC123")
        #DELL BSF
        login_page.complete_and_sumbit("mmikkan", "cardaABC123")

        home_page = Home(self.driver)
        assert home_page.lbl.text == "My page", "------------Houston we've got a problem--2----------"
        home_page.navigate_to_projects()

if __name__ == '__main__':
    unittest.main(verbosity=2)