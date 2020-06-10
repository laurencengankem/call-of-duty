'''
    This is the core of the requests module, given a session and the url it sends an HTTP get request to the API and
    returns the json.
'''
import click

def make_request(session, url):
    r = session.get(url)
    if r.status_code is not 200:
        click.secho(
            "\n [request.py]\t\tResponse is invalid, returned %s error. Check if the username is correct." %
            r.status_code,
            fg="green",
        )
    response_as_json = r.json()
    return response_as_json
