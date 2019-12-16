from urllib import parse


URL                     = 'https://www.instagram.com'
MEDIA_INFO              = '/p/%s/?__a=1'
MEDIA_BY_TAG            = '/explore/locations/%s/?__a=1'
ACCOUNT_INFO            = '/%s/?__a=1'
GENERAL_SEARCH          = '/web/search/topsearch/?context=blended&query=%s'
ACCOUNT_MEDIAS          = '/graphql/query/?query_id=17888483320059182&variables={"id": "%s","first":20,"after":%s}'
MEDIA_BY_LOCATION       = '/explore/locations/%s/%s/?__a=1'


def request_media_info(shortcode):
    return URL + MEDIA_INFO % parse.quote_plus(shortcode)


def request_media_by_tag(tag):
    return URL + MEDIA_BY_TAG % parse.quote_plus(tag)


def request_account_info(username):
    return URL + ACCOUNT_INFO % parse.quote_plus(username)


def request_general_search(search):
    return URL + GENERAL_SEARCH % parse.quote_plus(search)


def request_account_medias(user_id, cursor):
    return URL + ACCOUNT_MEDIAS % (str(user_id), cursor)

def request_media_by_location(location_id, location_name):
    return URL + MEDIA_BY_LOCATION % parse.quote_plus(str(location_id), location_name)


'''nome= input("insert the account name:  ")
nome.replace(" ", "")
url= request_media_info(nome)
print(url)'''

