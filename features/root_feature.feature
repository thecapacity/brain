Feature: Testing the Flask app

    Scenario: Visiting the Home Page
        Given the Flask app is running
        When I visit the home page
        Then I should see "Hello, World!"
