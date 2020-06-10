import requests
from requests.auth import HTTPBasicAuth
'''
    This is the core of the requests module, given a session and the url it sends an HTTP get request to the API and
    returns the json.
'''
import click

def make_request(session, url):
    #r = session.get(url)
    r=requests.get("https://www.instagram.com/sarapizzz/?__a=1",auth=HTTPBasicAuth('laurencengankem@yahoo.fr', 'lol.1967'))
    #print(r.json())
    if r.status_code is not 200:
        click.secho(
            "\n [request.py]\t\tResponse is invalid, returned %s error. Check if the username is correct." %
            r.status_code,
            fg="green",
        )
    print(r._content)
    response_as_json = r.json()

    return response_as_json
