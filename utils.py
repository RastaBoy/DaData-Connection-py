def get_addresses(response:dict):
    addresses = list()
    for item in response:
        for key in item:
            if key == 'unrestricted_value':
                addresses.append(item[key])
    return addresses

