from tmsangular.page_objects.base_page_tms_po import BasePage
from tmsangular.page_objects.commercial.clients_tms_po import Clients
from selenium.webdriver.common.by import By


class Login(BasePage):
    def __init__(self, driver):
        super(Login, self).__init__(driver)
        self.driver = driver


    def complete_and_sumbit(self, user, password):
        txf_username_we = self.driver.find_element(By.XPATH, "//*[@id='username']")
        txf_username_we.clear()
        txf_username_we.send_keys(user)

        txf_password_we = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/div[2]/div/app-login/div/div/form/div/div[2]/span/input")
        txf_password_we.clear()
        txf_password_we.send_keys(password)

        btn_submit_we = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/div[2]/div/app-login/div/div/form/div/div[5]/button/span")
        btn_submit_we.click()



