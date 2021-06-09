import requests

def get_response(params:dict, data:str):
    url = params['URL']
    token = params['API']
    lang = params['language']
    #print(f"{url} --- {token} -- {lang}")
    
    response = requests.post(url, 
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {token}",
        },
        json=data
    )

    response = response.json()
    response = response['suggestions']

    return response


