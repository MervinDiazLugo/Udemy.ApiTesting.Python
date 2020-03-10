@Twitter
Feature: Test Twitter


  @GetToken
  Scenario: Get Access token
    Given I connect with endpoint 1.1/search/tweets.json?q=from%3AEscenario:User_Test1&result_type=mixed&count=2
    When I login in Twitter App
    Then I do a Get
    And I print out the results of the response
    Then I compare response in entity statuses.created_at is Fri Mar 06 11:00:00 +0000 2020
    Then I compare response in entity statuses.id is 1235882821434183681
    Then I compare response in entity statuses.entities.hashtags is []
    Then I compare response in entity statuses.entities.media[0].id is 1235629131221647364
    Then I compare response in entity statuses.entities.media[0].media_url is http://pbs.twimg.com/media/ESXWJfCXQAQs6xr.jpg
    Then I compare response in entity statuses.extended_entities.media[0].id is 1235629131221647364
    Then I compare <Entity> show the values <Value>
      | Entity                                              | Value                                           |
      | statuses.entities.media[0].media_url                | http://pbs.twimg.com/media/ESXWJfCXQAQs6xr.jpg  |
      | statuses.extended_entities.media[0].id              | 1235629131221647364                             |