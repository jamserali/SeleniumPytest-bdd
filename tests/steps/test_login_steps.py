from pytest_bdd import given, when, then, scenarios, parsers
import logging
from pages.home_page import HomePage
from pages.login_page import LoginPage

scenarios("../features/user_login.feature")

logger = logging.getLogger(__name__)


@given("User is on login page")
def step1(browser):
    browser.get("https://naveenautomationlabs.com/opencart/index.php?route=common/home")


@when(parsers.parse("user enter valid {email} and {password}"))
def step2(browser, email, password, logger):
    home_page = HomePage(browser, logger)
    login_page = LoginPage(browser, logger)

    logger.info("Select login dropdown")
    home_page.select_login()
    login_page.do_login(email, password)


@then("user should be logged in Successful")
def step3(browser, logger):
    home_page = HomePage(browser, logger)
    login_page = LoginPage(browser, logger)

    assert login_page.verify_is_my_order_present() == "My Orders", \
        "My order text is not present in Main page"

    home_page.logout()
