from selenium.webdriver.common.by import By
from utils.page_actions import PageActions


class LoginPage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.PageActions = PageActions(driver)

        self.email_inp = (By.ID, "input-email")
        self.password_inp = (By.ID, "input-password")
        self.login_btn = (By.XPATH, "//input[@value='Login']")
        self.my_order_txt = (By.XPATH, "//*[@id='content']//h2[text()='My Orders']")

    def do_login(self, email, password):
        self.PageActions.send_key(self.email_inp, email)
        self.logger.info(f"Enter Email {email}")
        self.PageActions.send_key(self.password_inp, password)
        self.logger.info("Enter Password")
        self.PageActions.click(self.login_btn)
        self.logger.info("Click on Login button")

    def verify_is_my_order_present(self):
        return self.PageActions.get_text(self.my_order_txt)
