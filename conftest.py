from datetime import datetime
import os
import allure
import pytest_html
import pytest
import logging
import base64
from utils.browser_factory import BrowserFactory


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    logger = logging.getLogger("Bdd_Steps")
    logger.info("✅ Opening Browser...")
    driver = BrowserFactory.get_driver("chrome", True)
    request.session._driver = driver
    yield driver
    logger.info("❌ Quiting Browser...")
    driver.quit()


# html & Allure report hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        rep.extras = getattr(rep, "extras", [])
        if rep.failed:
            # Create timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            rep.extras.append(pytest_html.extras.html("❌ FAILED"))
            screenshot_dir = "screenshots"
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            os.makedirs(screenshot_dir, exist_ok=True)
            driver = item.session._driver
            driver.save_screenshot(file_path)

            with open(file_path, "rb") as f:
                image_bytes = f.read()
                encoded = base64.b64encode(image_bytes).decode("utf-8")

            rep.extras.append(
                pytest_html.extras.image(
                    encoded,
                    mime_type="image/png",
                    extension="png"
                )
            )
            allure.attach(
                image_bytes,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        elif rep.passed:
            rep.extras.append(pytest_html.extras.html("✅ PASSED"))


@pytest.fixture
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
