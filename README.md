This is an end-to-end UI automation framework built using Selenium with PyTest-BDD.
It is designed to provide a robust, scalable, and maintainable test automation solution for web applications.

The framework includes powerful features such as:

Behavior-Driven Development (BDD) using Gherkin feature files
Page Object Model (POM) for clean and reusable test design
Detailed logging for better debugging and traceability
HTML and Allure reports for rich and interactive test execution insights
Automatic screenshot capture on test failures, attached to both HTML and Allure reports
Parallel test execution for faster feedback
Jenkins pipeline integration for Continuous Integration and automated execution

NOTE: This framework is ideal for teams looking to implement a modern, CI-ready UI automation
 solution with high visibility, reliability, and easy maintenance.
    

#Create and Activate venv:
python -m venv venv
venv\Scripts\activate



#Test execution:
pytest --alluredir=allure-results


#For parallel execution :
pytest -n 4 --alluredir=allure-results

#For allure report :
allure serve allure-results

