import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json_Data = basedir + u"/data/"
    data_body = basedir + u"/data/data_body"
    data_responses = basedir + u"/data/data_responses"

    Environment = 'PetStore.test'
    #'PetStore.test'
    #"Twitter.test"

    if Environment == 'PetStore.test':
        # API
        API_hostAddressBase = "https://petstore.swagger.io/v2/"

        API_headers = {
            'version': '1.0-preview.1',
            'content-type': 'application/json',
        }

        API_body = {}
        API_subBody_dict = {}
        API_subBody_array = []

        Scenary = {
            'pet' : '20',
            'data': 'Hello'
        }

        DB_DRIVER = "DRIVER={PostgreSQL Unicode};"
        DB_HOST = "localhost"
        DB_PORT= "5432"
        DB_USER = "postgres"
        DB_PASS = "postgres"
        DB_DATABASE = "curso_api"

    if Environment == 'Twitter.test':
        # API
        API_hostAddressBase = "https://api.twitter.com/"

        api_key = "QlyoXK3iIUw5Nm3W8Bgsanqys"
        api_secret = "kAm5eRDyMWqZ3SAJA90IvFjFgfwL2BRWAIY15nI4JWHxBQeMl3"

        API_headers = {"Content-Type": "application/json"}

        API_body = {}
        API_subBody_dict = {}
        API_subBody_array = []

        Scenary = {
            'User_Test1' : 'StevenWilsonHQ',
            'User_Test2': 'mysquality'
        }

        DB_DRIVER = "DRIVER={PostgreSQL Unicode};"
        DB_HOST = "localhost"
        DB_PORT= "5432"
        DB_USER = "postgres"
        DB_PASS = "postgres"
        DB_DATABASE = "curso_api"