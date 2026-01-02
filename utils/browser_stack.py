import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserStack:

    @staticmethod
    def create_browserstack_driver():
        # username = os.getenv("BROWSERSTACK_USERNAME")
        # access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
        username = "jamserali_6H9x0UrVwQ7"
        access_key = "7xKktyCVs4xeq5yxE3dr"

        if not username or not access_key:
            raise Exception("BrowserStack credentials not set")

        options = Options()

        # BrowserStack W3C capabilities
        bstack_options = {
            "os": "Windows",
            "osVersion": "11",
            "browserName": "Chrome",
            "browserVersion": "latest",
            "projectName": "Selenium Pytest BDD ",
            "buildName": "PyTest Build",
            "sessionName": "BDD Tests",
            "seleniumVersion": "4.15.0"
        }

        options.set_capability("bstack:options", bstack_options)

        url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"
        # url="http://jamserali_y03gdr.browserstack.com"

        return webdriver.Remote(
            command_executor=url,
            options=options
        )
