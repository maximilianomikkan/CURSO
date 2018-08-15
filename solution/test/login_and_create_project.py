from solution.page_objects.login_po import Login
from solution.page_objects.projects_po import Projects
from solution.page_objects.home_po import Home
from solution.page_objects.base_page_po import BasePage
import unittest


class LoginAndCreateProject(BasePage):

    def test_login_and_create_project(self):

        #######LOGIN#######
        login_page = Login(self.driver)

        # MACBOOK
        # login_page.complete_and_sumbit("maximilianomikkan", "cardaABC123")
        # DELL BSF
        login_page.complete_and_sumbit("mmikkan", "cardaABC123")
        home_page = Home(self.driver)
        assert home_page.lbl.text == "My page", "------------Houston we've got a problem--1----------"

        #######PROJECT#######
        project_page = Projects(self.driver)

        home_page.navigate_to_projects()
        project_page.navigate_to_new_projects()
        assert project_page.search_field_new_project_tittle.text == "New project", "------------Houston we've got a problem--2----------"
        project_page.complete_new_project_form()
        assert project_page.search_field_project_was_created.text == "Successful update.", "------------Houston we've got a problem--3----------"
        project_page.navigate_to_projects()

if __name__ == '__main__':
    unittest.main(verbosity=2)