import requests

URL = 'https://lichess.org/api/user/'
USERNAME = ''

URL += USERNAME

def isOnline(url = URL):
    r = requests.get(URL)
    data = r.json()

    return data['online']
