from urllib import parse

BASE_URL                = 'https://www.instagram.com'
MEDIA_INFO              = '/p/%s/?__a=1'
MEDIA_BY_TAG            = '/explore/locations/%s/?__a=1'
ACCOUNT_INFO            = '/%s/?__a=1'
GENERAL_SEARCH          = '/web/search/topsearch/?context=blended&query=%s'
MEDIA_BY_ID             = '/graphql/query/?query_id=17888483320059182&variables={"id": "%s","first":50,"after":%s}'
MEDIA_BY_LOCATION       = '/explore/locations/%s/%s/?__a=1'
COMMENT_BY_SHORTCODE    = '/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={"shortcode":"%s", "first":50,"after":"%s"}'
MEDIA_BY_HASHTAG        = '/graphql/query/?query_hash=3e7706b09c6184d5eafd8b032dbcf487&variables={"tag_name":"%s","first":25,"after":"%s"}'


def request_media_info(shortcode):
    return BASE_URL + MEDIA_INFO % parse.quote_plus(shortcode)


def request_media_by_tag(tag):
    return BASE_URL + MEDIA_BY_TAG % parse.quote_plus(tag)


def request_account_info(username):
    return BASE_URL + ACCOUNT_INFO % parse.quote_plus(username)


def request_general_search(search):
    return BASE_URL + GENERAL_SEARCH % parse.quote_plus(search)


def request_account_medias(user_id, cursor):
    return BASE_URL + MEDIA_BY_ID % (str(user_id), cursor)


def request_media_by_location(location_id, location_name):
    return BASE_URL + MEDIA_BY_LOCATION % parse.quote_plus(str(location_id), location_name)


def request_comment(shortcode, cursor):
    return BASE_URL + COMMENT_BY_SHORTCODE % (shortcode, cursor)


def request_hashtag_media(hashtag, cursor):
    return BASE_URL + MEDIA_BY_HASHTAG % parse.quote_plus(hashtag, cursor)

