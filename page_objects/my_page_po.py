from page_objects.base_page_po import BasePage

class MyPage(BasePage):

    def __init__(self, driver):
        super(MyPage, self).__init__(driver)