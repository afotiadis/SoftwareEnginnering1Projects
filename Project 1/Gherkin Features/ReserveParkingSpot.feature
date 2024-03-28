Feature: Reserve a parking spot
    
    Background:
      Given I am the user
      And I am on the homepage
      
    Scenario:Succefully reserve a parking spot
      When I select a parking spot
      And the spot is available
      Then the system should reserve the spot 
      And I should see the message "Spot Reserved!"
      And I should be promted to enter the <reservation info>
        |date|start time|duration|
      And the <reservation info> should be added to the reservation
      And I should see the message "Information saved!"
      And I should return to the homepage
      
    Scenario:Parking spot is occupied 
      When I select a parking spot
      But the spot is occupied
      Then I should see the message "Spot is full! Select a different spot."
      And I should be able to select another parking spot
      
    