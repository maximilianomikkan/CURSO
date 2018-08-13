import time
from page_objects.base_page_po import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.driver = driver


    def complete_and_sumbit(self, user, password):
        #txf_username_we = self.driver.find_element(By.XPATH, "//*[@id='username']")
        self.txf_username_we = self.driver.find_element_by_id("username")
        #txf_username_we = self.driver.find_element(By.ID, "username")
        self.txf_username_we.clear()
        self.txf_username_we.send_keys(user)
        txf_password_we = self.driver.find_element(By.XPATH, "//*[@id='password']")
        txf_password_we.clear()

        # cargo los text fields
        # txf_username_we.send_keys(user)
        # txf_password_we.send_keys(password)

        txf_password_we.send_keys(password)

        # hago clic en el boton Acceder
        btn_submit_we = self.driver.find_element(By.XPATH, "//*[@id='login-submit']")
        btn_submit_we.click()
