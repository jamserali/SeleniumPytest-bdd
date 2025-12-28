from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserFactory:

    @staticmethod
    def get_driver(browser_name: str, headless: bool = False):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless")
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

            driver = webdriver.Chrome(
                service=ChromeService(),
                options=options
            )

        elif browser_name == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")
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

            options.set_preference("dom.webnotifications.enabled", False)

            driver = webdriver.Firefox(
                service=FirefoxService(),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser {browser_name}")

        return driver
