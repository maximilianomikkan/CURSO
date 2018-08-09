from page_objects.login_po import Login
from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By
import unittest

class myTests(BasePage):

    def test_login_redmine(self):
        print("---test_login_redmine---")
        login_page = Login(self.driver)
        login_page.complete_and_sumbit("maximilianomikkan", "cardaABC123")

        self.lbl = self.driver.find_element_by_xpath("//*[@id='content']/h2")
        assert self.lbl.text == "My page", "------------Houston we've got a problem--2----------"

if __name__ == '__main__':
    unittest.main(verbosity=2)