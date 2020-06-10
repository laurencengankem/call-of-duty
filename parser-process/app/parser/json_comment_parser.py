def edge_post_comment_count(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['count']


def comment_has_next_page(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['has_next_page']


def comment_end_cursor(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']


def comment_id(data):
    return data['node']['id']


def comment_text(data):
    return data['node']['text']


def comment_created_at(data):
    return data['node']['created_at']


def comment_owner_id(data):
    return data['node']['owner']['id']


def comment_owner_username(data):
    return data['node']['owner']['username']


def comment_post_edge_media_to_comment(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['edges']