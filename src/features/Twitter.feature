@Twitter
Feature: Test Twitter


  @GetToken
  Scenario: Get Access token
    Given I connect with endpoint 1.1/search/tweets.json?q=from%3AEscenario:User_Test1&result_type=mixed&count=2
    When I login in Twitter App
    Then I do a Get
    And I print out the results of the response
    Then I compare response in entity statuses.created_at is NOT NULL
    Then I compare response in entity statuses.id is 1257967132639473670
    Then I compare response in entity statuses.entities.hashtags is []
    Then I compare <Entity> show the values <Value>
      | Entity                                              | Value                  |
      | statuses.user.favourites_count                      | 3                      |
      | statuses.truncated                                  | True                   |

  Scenario: GET Single user by Username2
    Given I connect with endpoint labs/2/users/by/username/assassinsspain?user.fields=created_at,description,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified
    When I login in Twitter App
    When I do a Get
    Then I print out the results of the response
    And I assert that response in entity data path name is Assassin's Creed ES
    Then I compare <Entity> show the values <Value>
      | Entity                                | Value    |
      | data.created_at                       | NOT NULL |
      | data.description                      | NOT NULL |
      | data.id                               | NOT NULL |
      | data.location                         | España   |
      | data.name                             | Assassin's Creed ES|
      | data.public_metrics.followers_count   | 144027 |
      | data.public_metrics.tweet_count       | NOT NULL |
      | data.url                              | NOT NULL |
      | data.username                         | NOT NULL |
      | data.verified                         | True     |
