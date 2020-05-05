@Twitter
Feature: Test Twitter


  @GetToken
  Scenario: Get Access token
    Given I connect with endpoint 1.1/search/tweets.json?q=from%3AEscenario:User_Test1&result_type=mixed&count=2
    When I login in Twitter App
    Then I do a Get
    And I print out the results of the response
    Then I compare response in entity statuses.created_at is NOT NULL
    Then I compare response in entity statuses.id is 1256126779049291777
    Then I compare response in entity statuses.entities.hashtags is []
    Then I compare <Entity> show the values <Value>
      | Entity                                              | Value                  |
      | statuses.user.favourites_count                      | 3                      |
      | statuses.truncated                                  | True                   |

