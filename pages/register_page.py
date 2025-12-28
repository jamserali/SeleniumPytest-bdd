from selenium.webdriver.common.by import By
from utils.page_actions import PageActions


class RegisterPage:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.PageActions = PageActions(driver)

        self.first_name_inp = (By.ID, "input-firstname")
        self.last_name_inp = (By.ID, "input-lastname")
        self.email_inp = (By.ID, "input-email")
        self.telephone_inp = (By.ID, "input-telephone")
        self.password_inp = (By.ID, "input-password")
        self.confirm_pass_inp = (By.ID, "input-confirm")
        self.privacy_policy_chk = (By.NAME, "agree")
        self.continue_btn = (By.XPATH, "//input[@value='Continue']")

    def do_register(self, fname, lname, email, telephone, password):
        self.PageActions.send_key(self.first_name_inp, fname)
        self.logger.info(f"User enters First Name {fname}")

        self.PageActions.send_key(self.last_name_inp, lname)
        self.logger.info(f"User enters Last Name {lname}")

        self.PageActions.send_key(self.email_inp, email)
        self.logger.info(f"User enters Email {email}")

        self.PageActions.send_key(self.telephone_inp, telephone)
        self.logger.info(f"User enters Telephone {telephone}")

        self.PageActions.send_key(self.password_inp, password)
        self.logger.info("User enters Password")

        self.PageActions.send_key(self.confirm_pass_inp, password)
        self.logger.info("User enters Confirm Password")

        self.PageActions.click(self.privacy_policy_chk)
        self.logger.info("User accepted Privacy Policy")

        self.PageActions.click(self.continue_btn)
        self.logger.info("User clicked Continue")
