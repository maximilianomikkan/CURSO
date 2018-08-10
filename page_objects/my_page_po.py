from page_objects.base_page_po import BasePage


class MyPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        self.lbl2 = self.driver.find_element_by_xpath("//*[@id='content']/h2")