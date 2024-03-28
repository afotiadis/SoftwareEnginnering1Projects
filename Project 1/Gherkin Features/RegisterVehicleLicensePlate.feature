Feature: Register vehicle's license plate
  
  Background:
    Given that I am the user

  Scenario:Succefully register a vehicle's license plate
    When I sumbit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    Then I should see the message "Succesful registration!"
    And I should return to the homepage

  Scenario:Duplicate registration
    When I sumbit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    But the vehicle's license plate has already registered
    Then I should see the message "The registration already exists!"
    And I should be prompted to submit a new registration
    
  Scenario:Invalid registration
    When I submit a vehicle's <license plate>
    |plate's name|'AKH1234'|
    But the vehicle's license plate is invalid
    Then I should see the message "Invalid registration!"
    And I should be prompted to submit a new registration
    
  