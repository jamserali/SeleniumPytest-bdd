from selenium.webdriver.common.by import By
from utils.page_actions import PageActions


class HomePage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.PageActions = PageActions(driver)

        self.my_account = (By.LINK_TEXT, "My Account")
        self.register_option = (By.LINK_TEXT, "Register")
        self.login_option = (By.LINK_TEXT, "Login")
        self.logout_option = (By.LINK_TEXT, "Logout")

    def select_register(self):
        self.PageActions.click(self.my_account)
        self.logger.info("Click on 'My Account' dropdown")
        self.PageActions.click(self.register_option)
        self.logger.info("Selected Register option from 'My Account' dropdown")

    def select_login(self):
        self.PageActions.click(self.my_account)
        self.logger.info("Click on 'My Account' dropdown")
        self.PageActions.click(self.login_option)
        self.logger.info("Click on Login option")

    def logout(self):
        self.PageActions.click(self.my_account)
        self.logger.info("Click on 'My Account' dropdown")
        self.PageActions.click(self.logout_option)
        self.logger.info("Click on Logout option")
