from urllib import parse
import urllib.request, json
from kivy.network.urlrequest import UrlRequest

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


'''profile = input("enter the profile name8 \t")
profile.replace(" ", "")

urli=request_account_info(profile)
print(urli)
data={}

with urllib.request.urlopen(urli) as url:
    data = json.loads(url.read().decode())

print(data)
print(data['graphql']['user']['edge_followed_by']['count'])
print(data['graphql']['user']['edge_follow']['count'])
print(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
print(data['graphql']['user']['profile_pic_url'])'''

