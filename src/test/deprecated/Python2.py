import re
import datetime


API_hostAddressBase = u'https://petstore.swagger.io/v2'
partHost = "\endpoint\FECHA\Scenario:Today"

def get_full_host(_PartHost):
    _RegexPartHost = str(replace_with_context_values(_PartHost))
    _endpoint = API_hostAddressBase + _RegexPartHost
    print(_endpoint)
    return _endpoint


def replace_with_context_values(text):
    PatronDeBusqueda = r"(?<=Scenario:)\w+"
    variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
    for variable in variables:
        if variable == 'Today':
            dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
            text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
            continue
    return text

endpoint = get_full_host(partHost)