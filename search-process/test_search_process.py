import requests

'''*
    This unit test the search_process to check wether it returns an error  when no username
    is specified in the url and return a file whenever there are some data stored in the database for the specified username
'''
def test_search_process():
    r = requests.get('http://localhost:5000')
    print(r.text)
    assert  r.status_code==404
    assert  r.text== "Requested page is not available, contact the site administrator"

    r = requests.get('http://localhost:5000/s/sarpizzz')
    assert r.status_code== 404
    assert  r.text== "Username not found"

    r = requests.get('http://localhost:5000/s/sarapizzz')
    assert r.status_code== 200
    result= r.json()
    assert result['username']== 'sarapizzz'
