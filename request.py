import requests

def send_request(params:dict, query:str):
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
        json={
            'query' : query,
            'language' : lang
        }
    )

    answer = list()

    response = response.json()
    response = response['suggestions']

    for item in response:
        for key in item:
            if key == 'unrestricted_value':
                answer.append(item[key])
    
    #print(answer)

    return answer


