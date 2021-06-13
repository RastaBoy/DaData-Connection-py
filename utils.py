import os

def get_addresses(response:dict):
    addresses = list()
    for item in response:
        if item['data']['postal_code'] != None:
            addresses.append(item['unrestricted_value'])
    return addresses


def get_coordinates(response:dict):
    response = response[0]['data']
    result = (response['geo_lat'], response['geo_lon'], )
    return result


def printer(text:str, *, result=None):
    os.system('cls')
    print(text)
    os.system("pause")
    return result


def dict_formater(obj:dict):
    result = ""
    for key in obj:
        result += f"'{key}' : '{obj[key]}' \n"
    return result
