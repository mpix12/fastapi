# Created by mandarpande at 13/1/23
Feature: TestHash
  # Enter feature description here

  Scenario: decrypt password
    Given I am on Blog docs page
    When I use page as 5
    And page_size as 10
    And Execute /blog/all_details
    Then I should get response as 200
