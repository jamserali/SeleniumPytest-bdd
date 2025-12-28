Feature: Login Functionality

Scenario Outline: Successful Login
  Given User is on login page
  When user enter valid <email> and <password>
  Then user should be logged in Successful

Examples:
| email             | password |
| test123@gmail.com | Test@123 |
| test123@gmail.com | Test@123 |
| test123@gmail.com | Test@123 |
| test123@gmail.com | Test@123 |
