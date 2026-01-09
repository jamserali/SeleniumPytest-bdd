import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserFactory:
    logger = logging.getLogger("Bdd_Steps")

    @staticmethod
    def create_local_driver(browser_name: str, headless: bool = False):
        browser_name = browser_name.lower()
        BrowserFactory.logger.info(f"✅ Running in Local Driver Browser...")


        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            if headless:
                options.add_argument("--headless")


            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.geolocation": 2,
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.media_stream_mic": 2,
                "profile.default_content_setting_values.popups": 2,
            }

            options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(
                service=ChromeService(),
                options=options
            )

        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")

            if headless:
                options.add_argument("--headless")

            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.geolocation": 2,
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.media_stream_mic": 2,
                "profile.default_content_setting_values.popups": 2,
            }

            options.set_preference("dom.webnotifications.enabled", False)

            driver = webdriver.Firefox(
                service=FirefoxService(),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser {browser_name}")

        return driver

    @staticmethod
    def create_browserstack_driver():
        # username = os.getenv("BROWSERSTACK_USERNAME")
        # access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
        BrowserFactory.logger.info(f"✅ Running in BrowserStack  Browser...")

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

        return webdriver.Remote(
            command_executor=url,
            options=options
        )

    @staticmethod
    def create_grid_driver(browser:str,headless: bool = False):
        BrowserFactory.logger.info(f"✅ Running in Selenium GRID Browser...")

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.geolocation": 2,
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.media_stream_mic": 2,
                "profile.default_content_setting_values.popups": 2,
            }
            options.add_experimental_option("prefs", prefs)


            if headless:
                options.add_argument("--headless")

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            if headless:
                options.add_argument("--headless")
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless")

        return webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )