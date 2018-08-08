import unittest
from features.environment import Environment
from page_objects.login_po import Login


class Login(unittest.TestCase):
    Environment.setUp()

    login = Login()
    home = login.login_redmine(self, "user", "pass")
    assert home.txf_home_loc.text == "Home"

    Environment.tearDown()