@Integration
Feature: Test WebApi

  @WebApi
  Scenario: GET pet data
    Given I connect with endpoint pet/Escenario:pet
    When I do a Get
    Then I print out the results of the response
    Then The api response is 200
    And I assert response in entity id is 20
    And I assert response in entity name is Mervin Alberto
    And I assert response in entity status is available
    And I assert that response in entity category path id is 10
    And I assert that response in entity photoUrls path 0 is Foto1
    And I assert that response in entity tags path 0 is {'id': 0, 'name': 'string'}
    Then The elements <Entity> show the values <Value>
      | Entity | Value          |
      | id     | 20             |
      | name   | Mervin Alberto |
      | status | available      |
    Then elements <Entity> in <Path> show the values <Value>
      | Entity      |Path   | Value   |
      | category    |   id  | 10      |
      | photoUrls   |   0   | Foto1   |
    Then I compare the json File data_responses/pet20 with response

  @WebApi
  Scenario: Retrieve pet data
    Given I connect with endpoint pet/10
    When I do a Get
    Then I print out the results of the response
    Then The api response 404 Dont Exist

  @WebApi
  Scenario: built body parameters data
    Given I connect with endpoint pet
    Then I set the entity id with the value 700
    Then I set the entity name with the value Mervin Alberto
    Then I set the entity status with the value available
    When I do a Put
    Then The api response is 200
    Then I print out the results of the response

  @WebApi
  Scenario: Get json as body parameters
    Given I connect with endpoint pet
    When I set the body with data_body/pet
    Then I set the entity id with the value 20
    Then I set the entity name with the value Mervin Alberto
    Then I set the entity status with the value available
    And I set sub entity id with the value 10
    And I set sub entity name with the value Billy Butcher
    Then I set sub body category
    And I append sub array value Foto10
    And I append sub array value Foto20
    Then I set sub array photoUrls
    When I do a Post
    Then The api response is 200
    Then I print out the results of the response

 @sql
 Scenario: Do a SQL Query
    Then I do a SQL query """SELECT * FROM public.my_api_categoria Where id = 2"""
    Then I set the entity name with the value Query:descripcion
    Then I set the entity codigo with the value Query:id