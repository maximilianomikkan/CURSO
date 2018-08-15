import unittest
from selenium import webdriver
import time
import random

#
# Login into the Redmine
# Click on Project Link
# Select an existing project
# Go to Settings tab
# Go to member
# On Members tab create a new member:
# Non member user
# Role: Reporter
# Bonus Track:
# Check if User was created successfully
# Create page_objects for each page


class SearchTests(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to Redmine Login  page
        self.driver.get("http://192.168.64.2/login/")


    def test_search_by_id(self):
        # get the USERNAME textbox
        self.search_field_username = self.driver.find_element_by_id("username")
        self.search_field_username.clear()

        # get the PASSWORD textbox
        self.search_field_password = self.driver.find_element_by_id("password")
        self.search_field_password.clear()

        # enter USERNAME keyword
        self.search_field_username.send_keys("maximilianomikkan")

        # enter PASSWORD keyword
        self.search_field_password.send_keys("cardaABC123")

        # get the LOGIN button
        self.search_field_login = self.driver.find_element_by_name("login")
        self.search_field_login.click()

        # ASSERT
        self.search_field_user_active = self.driver.find_element_by_xpath("//*[@id='loggedas']/a")
        assert self.search_field_user_active.text == "maximilianomikkan", "------------Houston we've got a problem--1----------"

# -------------------------------

        #
        # # click en IR AL PROYECTO
        # self.search_field_ir_al_proyecto = self.driver.find_element_by_xpath("//*[@id='project-jump']/span")
        # self.search_field_ir_al_proyecto.click()
        #
        # # click en IR AL PROYECTO
        # self.search_field_busqueda_proyecto = self.driver.find_element_by_id("projects-quick-search")
        # self.search_field_busqueda_proyecto.clear()
        # self.search_field_busqueda_proyecto.send_keys("Project 1")

        # click en Projects
        self.search_projects = self.driver.find_element_by_xpath("//*[@id='top-menu']/ul/li[3]/a")
        self.search_projects.click()

        # click en algun proyecto
        self.search_x_proyecto = self.driver.find_element_by_xpath("//*[@id='projects-index']/ul/li[2]/div/a")
        self.search_x_proyecto.click()

        # click en Configuraciones
        self.search_configuraciones = self.driver.find_element_by_xpath("//*[@id='main-menu']/ul/li[6]/a")
        self.search_configuraciones.click()

        # click en Miembros
        self.search_miembros = self.driver.find_element_by_id("tab-members")
        self.search_miembros.click()

        # click en Nuevo Miembros
        self.search_nuevo_miembro = self.driver.find_element_by_xpath("//*[@id='tab-content-members']/p/a")
        self.search_nuevo_miembro.click()

        time.sleep(6)




    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
