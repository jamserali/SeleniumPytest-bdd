from pytest_bdd import given, when, then, scenarios, parsers
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.utils import Utils

scenarios("../features/user_register.feature")


@given(parsers.cfparse('User is on register page "{url}"'))
def step1(browser, logger, url):
    browser.get(url)
    logger.info(f"Navigating to URL :: {url}")
    home_page = HomePage(browser, logger)
    home_page.select_register()


@when(parsers.parse("user enters {fname}, {lname}, {email}, {telephone}, {password}"))
def step2(browser, fname, lname, email, telephone, password, logger):
    register_page = RegisterPage(browser, logger)
    register_page.do_register(fname, lname, email, telephone, password)


@then("user should be registered Successful")
def step3(browser):
    pass
