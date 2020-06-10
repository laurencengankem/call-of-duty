def end_cursor(data):
    return data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def end_cursor_comment(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']


def id_number(data):
    return data['graphql']['user']['id']


def post_number(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['count']


def shortcode_list(data, n):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][n]['node']['shortcode']


def shortcode(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges']


def shortcode_url(data, n):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][n]['node']['display_url']


def post_location(data, i):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['location']


def is_private(data):
    return data['graphql']['user']['is_private']
