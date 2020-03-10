# -*- coding: utf-8 -*-
import pyodbc as pyodbc

import objectpath as objectpath
import pytest

from functions.Inicializar import Inicializar
import json
import requests
import re
import time
import datetime
import random
import string



##########################################################################
#########################   -=_WEB API TEST_=-   #########################
##########################################################################

class Functions():

    def ReplaceWithContextValues(self, text):
        PatronDeBusqueda = r"(?<=Escenario:)\w+"
        #r"(?<=Escenario:)\w+"
        variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
        self.N = 0
        for variable in variables:
            if variable == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
                text = re.sub('(Escenario:)'+ variable, dateToday, text, re.IGNORECASE)
                continue
            text = re.sub('(Escenario:)'+ variable, Inicializar.Scenary[variable], text, re.IGNORECASE)
        return text

    def ReplaceWithQueryValues(self, text):
        PatronDeBusqueda = r"(?<=Query:)\w+"
        variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
        for variable in variables:
            text = re.sub('Query:'+ variable, str(self.QUERY[variable]), text, re.IGNORECASE)
        return text

    def get_full_host(self, _PartHost):
        _RegexPartHost = str(Functions.ReplaceWithContextValues(self, _PartHost))
        self._endpoint = Inicializar.API_hostAddressBase + _RegexPartHost
        print(self._endpoint)
        return self._endpoint

    def do_a_get(self):
        new_header = Inicializar.API_headers
        self._response = requests.get(self._endpoint, headers=new_header)
        return self._response

    def print_api_response(self):
        self.json_response = json.loads(self._response.text)
        print(json.dumps(self.json_response, indent=3))

    def response_is(self, code):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == int(code), f'El codigo de respuesta no es el esperado {self._response.status_code} != {code}'

    def response_is_200(self):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == 200, f'El codigo de respuesta no es el esperado {self._response.status_code} != 200'

    def response_is_404(self):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == 404, f'El codigo de respuesta no es el esperado {self._response.status_code} != 404'

    def set_body_values(self, entity, value):
        def set_ramdon_values(self):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(6))

        if value.lower() == "random":
            value = set_ramdon_values(self)
            if entity.lower() == "email":
                value = set_ramdon_values(self) + "@udemy.com"

        value = Functions.ReplaceWithQueryValues(self, value)
        Inicializar.API_body[entity] = str(value)
        self._new_body = Inicializar.API_body
        print(self._new_body)
        return self._new_body

    def set_sub_body_dict_values(self, entity, value):
        Inicializar.API_subBody_dict[entity] = value
        print((json.dumps(Inicializar.API_subBody_dict, indent=4)))
        return Inicializar.API_subBody_dict

    def set_sub_body_dict(self, key):
        Inicializar.API_body[key] = Inicializar.API_subBody_dict
        print((json.dumps(self._new_body, indent=4)))
        Inicializar.API_subBody_dict = {}
        return Inicializar.API_subBody_dict

    def set_sub_body_array_values(self, value):
        Inicializar.API_subBody_array.append(value)
        print(Inicializar.API_subBody_array)
        return Inicializar.API_subBody_array

    def set_sub_body_array(self, key):
        Inicializar.API_body[key] = Inicializar.API_subBody_array
        print((json.dumps(self._new_body, indent=4)))
        Inicializar.API_subBody_array = []
        return Inicializar.API_subBody_array


    def get_json_inData(self, file):
        json_path = Inicializar.Json_Data + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_inData: " + file)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)

    def set_initial_json_body(self, file):
        self.New_Body = Functions.get_json_inData(self, file)
        Inicializar.API_body = self.New_Body
        print((json.dumps(Inicializar.API_body, indent=4)))

    def do_a_put(self):
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.put(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def do_a_post(self):
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.post(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def assert_response_expected(self, entity, expected, subPath = 0):
        self.json_response = json.loads(self._response.text)
        PATH_VALUE = self.json_response[entity]

        if expected == "NOT NULL":
            assert str(PATH_VALUE) != None, f"El valor es Null: {PATH_VALUE} != {expected}"
            return

        elif expected == "NULL":
            assert str(PATH_VALUE) == None, f"El valor no es Null: {PATH_VALUE} != {expected}"
            return
        else:
            lista =  isinstance(PATH_VALUE, list)
            dicts = isinstance(PATH_VALUE, dict)
            if lista:
                PATH_VALUE = self.json_response[entity][int(subPath)]
            if dicts:
                PATH_VALUE = self.json_response[entity][subPath]

            assert str(PATH_VALUE) == expected, f"El valor no es el esperado: {PATH_VALUE} != {expected}"

    def expected_results_value(self, file):
        self.json_strings = Functions.get_json_inData(self, file)
        try:
            assert self.json_strings == self.json_response
            print(u"Se cumplió con el valor esperado")
            verificar = True
        except AssertionError:
            verificar = False
            print("La respuesta fue: ")
            print(json.dumps(self.json_response, indent=4))
            print("Se esperaba: ")
            print(json.dumps(self.json_strings, indent=4))
            assert verificar == True

    def pyodbc_query(self, _query):
        self.conn = Functions.pyodbc_conn(self)
        if self.conn is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.description
                columns = [column[0] for column in self.Result]
                result = []
                for row in self.cursor.fetchall():
                    result.append(dict(zip(columns, row)))
                print(result[0])
                self.QUERY = result[0]
                return self.QUERY

            except (pyodbc.Error) as error:
                pytest.skip(f"Error en la consulta {error}")

            finally:
                if (self.conn):
                    self.cursor.close()
                    self.conn.close()
                    print("pyodbc Se cerró la conexion")

    def pyodbc_conn(self, _host = Inicializar.DB_HOST,_dbname=Inicializar.DB_DATABASE, _user = Inicializar.DB_USER, _pass = Inicializar.DB_PASS):
        try:
            self.conn = pyodbc.connect(
                f'{Inicializar.DB_DRIVER}'
                'Server='+ _host +';'
                'Database='+ _dbname +';'
                'uid='+ _user +';'
                'pwd='+ _pass +';'
                'Trusted_Connection=no'
            )
            self.cursor = self.conn.cursor()
            print("Always Connected")

        except (pyodbc.OperationalError) as error:
            self.conn = None
            self.cursor = None
            pytest.skip("Error en connection strings: " + str(error))

        return self.conn

    def new_compare_entity_values(self, path, esperado):
        esperado = str(esperado)
        try:
            tree_obj = objectpath.Tree(self.json_response)
            entity = tuple(tree_obj.execute('$.' + path))
            PATH_VALUE =  str(entity[0])
            print(entity)
        except SyntaxError:
            entity = str(None)
            print("No se pudo obtener ningun valor de la busqueda")

        if esperado == "NOT NULL":
            assert str(PATH_VALUE) != None, f"El valor es Null: {PATH_VALUE} != {expected}"
            return

        elif esperado == "NULL":
            assert str(PATH_VALUE) == None, f"El valor no es Null: {PATH_VALUE} != {expected}"
            return
        else:
            assert PATH_VALUE == esperado, f"No es el valor esperado {path}: {esperado} != {entity_R1}"
