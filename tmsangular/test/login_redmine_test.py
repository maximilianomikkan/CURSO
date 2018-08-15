from tmsangular.page_objects.login_tms_po import Login
from tmsangular.page_objects.home_tms_po import Home
from tmsangular.page_objects.base_page_tms_po import BasePage
import unittest

class myTests(BasePage):

    def test_login_redmine(self):
        print("---test_login_tms---")
        login_page = Login(self.driver)
        login_page.complete_and_sumbit("mmikkan", "bongOrno456")

        # home_page = Home(self.driver)
        # assert home_page.lbl.text == "My page", "------------Houston we've got a problem--2----------"
        # home_page.navigate_to_projects()

if __name__ == '__main__':
    unittest.main(verbosity=2)