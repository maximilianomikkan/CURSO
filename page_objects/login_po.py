import time
from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By



class Login(BasePage):

    def __init__(self, driver):
        self.driver = driver

        # Locators en Elements
        self.txf_username_loc = driver.find_element(By.XPATH, "//*[@id='username']")
        self.txf_password_loc = driver.find_element(By.XPATH, "//*[@id='password']")
        self.btn_submit_loc = driver.find_element(By.XPATH, "//*[@id='login-submit']")


    def complete_and_sumbit(self, username, password):
        # limpio los text fields
        self.txf_username_loc.clear()
        self.txf_password_loc.clear()

        # cargo los text fields
        self.txf_username_loc.send_keys(username)
        self.txf_password_loc.send_keys(password)

        # hago clic en el boton Acceder
        self.btn_submit_loc.click()





# METODO ANTERIOR LO DIVIDÍ EN 2 PARA USARLO CON LO DE BEHAVE..
    def complete(self, username, password):
        # limpio los text fields
        self.txf_username_loc.clear()
        self.txf_password_loc.clear()

        # cargo los text fields
        self.txf_username_loc.send_keys(username)
        self.txf_password_loc.send_keys(password)
        time.sleep(3)

    def sumbit(self):
        # hago clic en el boton Acceder
        self.btn_submit_loc.click()
