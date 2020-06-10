def post_count(data):
    return data['data']['user']['edge_owner_to_timeline_media']['count']


def post_page_info_has_next_page(data):
    return data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']


def post_page_info_end_cursor(data):
    return data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def post_edges(data):
    return data['data']['user']['edge_owner_to_timeline_media']['edges']


def post_id(data):
    return data['node']['id']


def post_typename(data):
    return data['node']['__typename']


def post_edge_media_to_caption_edges(data, i):
    return data['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges']


def post_edge_media_to_caption_text(data):
    return data['node']['edge_media_to_caption']['edges'][0]['node']['text']


def post_edge_media_to_caption_shortcode(data):
    return data['node']['shortcode']


def post_edge_media_to_comment(data):
    return data['node']['edge_media_to_comment']


def post_edge_media_to_comment_count(data):
    return data['node']['edge_media_to_comment']['count']


def post_comment_disabled(data):
    return data['node']['comments_disabled']


def post_taken_at_timestamp(data):
    return data['node']['taken_at_timestamp']


def post_dimensions(data):
    return data['node']['dimensions']


def post_height(data):
    return data['node']['dimensions']['height']


def post_width(data):
    return data['node']['dimensions']['width']


def post_display_url(data):
    return data['node']['display_url']


def post_edge_media_preview_like(data):
    return data['node']['edge_media_preview_like']


def post_edge_media_preview_like_count(data):
    return data['node']['edge_media_preview_like']['count']


def post_owner(data):
    return data['node']['owner']


def post_owner_id(data):
    return data['node']['owner']['id']


def post_thumbnail_src(data):
    return data['node']['thumbnail_src']


def post_is_video(data):
    return data['node']['is_video']


def post_video_view_count(data):
    return data['node']['video_view_count']


