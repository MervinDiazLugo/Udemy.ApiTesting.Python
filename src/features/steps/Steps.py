# -*- coding: utf-8 -*-
from behave import *
import pytest
import unittest
import requests
import json
from behave import *
from functions.Functions import Functions
from functions.Inicializar import Inicializar
use_step_matcher("re")

class StepsDefinitions():
#######################################################
############### _ = - WEB API - = _ ###################
#######################################################

    @step('I connect with endpoint (.*)')
    def step_impl(self, host):
        self._endpoint = Functions.get_full_host(self, host)
        return self._endpoint

    @step("I do a Get")
    def step_impl(self):
        self._response = Functions.do_a_get(self)
        return self._response

    @step("I print out the results of the response")
    def step_impl(self):
        Functions.print_api_response(self)

    @then("The api response is (.*)")
    def step_impl(self, code):
        Functions.response_is(self, code)

    @then("The api response 200 Ok")
    def step_impl(self):
        Functions.response_is_200(self)

    @then("The api response 404 Dont Exist")
    def step_impl(self):
        Functions.response_is_404(self)

    @step("I set the entity (.*) with the value (.*)")
    def step_impl(self, entity, value):
        Functions.set_body_values(self, entity, value)

    @step("I set sub entity (.*) with the value (.*)")
    def step_impl(self, entity, value):
        Functions.set_sub_body_dict_values(self, entity, value)

    @step("I append sub array value (.*)")
    def step_impl(self, value):
        Functions.set_sub_body_array_values(self, value)

    @step("I set sub body (.*)")
    def step_impl(self, key):
        Functions.set_sub_body_dict(self, key)

    @step("I set sub array (.*)")
    def step_impl(self, key):
        Functions.set_sub_body_array(self, key)

    @when("I set the body with (.*)")
    def step_impl(self, file):
        Functions.set_initial_json_body(self, file)

    @when("I do a Put")
    def step_impl(self):
        Functions.do_a_put(self)

    @when("I do a Post")
    def step_impl(self):
        Functions.do_a_post(self)

    @step("I assert response in entity (.*) is (.*)")
    def step_impl(self, entity, expected):
        Functions.assert_response_expected(self, entity, expected)

    @step("I assert that response in entity (.*) path (.*) is (.*)")
    def step_impl(self, entity, subPath, expected):
        Functions.assert_response_expected(self, entity, expected, subPath)

    @step("The elements (.*) show the values (.*)")
    def step_impl(self, entity, expected):
        for row in self.table:
            entity = row['Entity']
            value = row['Value']
            Functions.assert_response_expected(self, entity, value)

    @step("elements (.*) in (.*) show the values (.*)")
    def step_impl(self, entity, subPath, expected):
        for row in self.table:
            print(row)
            entity = row['Entity']
            subPath = row['Path']
            value = row['Value']
            Functions.assert_response_expected(self, entity, value, subPath)


    @then("I compare the json File (.*) with response")
    def step_impl(self, file):
        Functions.expected_results_value(self, file)

    @then('I do a SQL query """(.*)"""')
    def step_impl(self, _query):
        self._Result = Functions.pyodbc_query(self, _query)


    @step("I login in Twitter App")
    def step_impl(self):
        body = {"grant_type": "client_credentials"}
        response = requests.post(Inicializar.API_hostAddressBase + "oauth2/token", auth=(Inicializar.api_key, Inicializar.api_secret), data=body)
        Autorization_response = json.loads(response.text)
        print(Autorization_response['access_token'])
        Inicializar.API_headers["Authorization"] = "Bearer " + Autorization_response['access_token']


    @then("I compare response in entity (.*) is (.*)")
    def step_impl(self, entity, expected):
        Functions.new_compare_entity_values(self, entity, expected)


    @then("I compare (.*) show the values (.*)")
    def step_impl(self, entity, expected):
        for row in self.table:
            entity = row['Entity']
            value = row['Value']
            Functions.new_compare_entity_values(self, entity, value)