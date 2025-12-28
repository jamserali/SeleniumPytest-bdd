Feature: Register Functionality

  Scenario Outline: Successful Register
    Given User is on register page "https://naveenautomationlabs.com/opencart/index.php?route=common/home"
    When user enters <fname>, <lname>, <email>, <telephone>, <password>
    Then user should be registered Successful

    Examples:
      | fname   | lname  | email               | telephone  | password |
      | Jamser  | Ali    | test123@gmail.com   | 8903673920 | Test@123 |
      | Abhijit | Kumar  | abhijit23@gmail.com | 8903673920 | Test@123 |
      | Nomad   | Rasid  | ayaz123@gmail.com   | 8903673920 | Test@123 |
      | Sneha   | Bhusan | sweta123@gmail.com  | 8903673920 | Test@123 |
      | Kiran   | Kumar  | kiran123@gmail.com  | 8903673920 | Test@123 |
      | Dilip   | Kumar  | dileep123@gmail.com | 8903673920 | Test@123 |
