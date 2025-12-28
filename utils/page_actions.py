from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class PageActions:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_key(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self._find(locator).text

    def is_displayed(self, locator):
        try:
            return self._find(locator).is_displayed()
        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        return self._find(locator).get_attribute(attribute)

    def scroll_to_element(self, locator):
        element = self._find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
