def end_cursor(data):
   return data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def end_cursor_comment(data):
    return data['data']['shortcode_media']['edge_media_to_comment']['page_info']['end_cursor']


#def end_cursor(data):
#    return data['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def edge_post(data):
    return data['data']['user']['edge_owner_to_timeline_media']['edges']


def like_number(data):
    return data['node']['edge_media_preview_like']['count']


def comment_number(data):
    return data['node']['edge_media_to_comment']['count']


def username(data):
    return data['graphql']['user']['username']


def fullname(data):
    return data['graphql']['user']['full_name']


def followers(data):
    return str(data['graphql']['user']['edge_followed_by']['count'])


def following(data):
    return str(data['graphql']['user']['edge_follow']['count'])


def id_number(data):
    return data['graphql']['user']['id']


def is_verified(data):
    return data['graphql']['user']['is_verified']


def biography(data):
    return data['graphql']['user']['biography']


def is_business(data):
    return data['graphql']['user']['is_business_account']


def business_category(data):
    return data['graphql']['user']['business_category_name']


def is_private(data):
    return data['graphql']['user']['is_private']


def post_number(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['count']


def shortcode(data):
    return data['node']['shortcode']


def profile_pic(data):
    return data['graphql']['user']['profile_pic_url_hd']


#boolean
def show_suggested_profiles(data):
    return data['show_suggested_profiles']


def blocked_by_viewer(data):
    return data['graphql']['user']['blocked_by_viewer']


def show_follow_dialog(data):
    return data['show_follow_dialog']


def country_block(data):
    return data['graphql']['user']['country_block']


def followed_by_viewer(data):
    return data['graphql']['user']['followed_by_viewer']


def follows_viewer(data):
    return data['graphql']['user']['follows_viewer']


def has_channel(data):
    return data['graphql']['user']['has_channel']


def has_blocked_viewer(data):
    return data['graphql']['user']['has_blocked_viewer']


def has_requested_viewer(data):
    return data['graphql']['user']['has_requested_viewer']


def is_joined_recently(data):
    return data['graphql']['user']['is_joined_recently']


def requested_by_viewer(data):
    return data['graphql']['user']['requested_by_viewer']


def connected_fb_page(data):
    return data['graphql']['user']['connected_fb_page']


def edge_felix_video_timeline_count(data):
    return data['graphql']['user']['edge_felix_video_timeline']['count']


def edge_felix_video_timeline_has_next_page(data):
    return data['graphql']['user']['edge_felix_video_timeline']['page_info']['has_next_page']


def edge_felix_video_timeline_end_cursor(data):
    return data['graphql']['user']['edge_felix_video_timeline']['page_info']['end_cursor']


#number of posts già fatto sopra
def edge_owner_to_timeline_media_count(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['count']


def edge_owner_to_timeline_media_has_next_page(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']


#già fatto sopra
def edge_owner_to_timeline_media_end_cursor(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']


def post_typename(data):
    return data['node']['__typename']


def post_id(data):
    return data['node']['id']


def post_0_shotcode(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']


def post_comment_count(data):
    return data['node']['edge_media_to_comment']['count']


def post_comments_disabled(data):
    return data['node']['comments_disabled']


def post_taken_at_timestamp(data):
    return data['node']['taken_at_timestamp']


def post_dimensions_height(data):
    return data['node']['dimensions']['height']


def post_dimensions_width(data):
    return data['node']['dimensions']['width']


################################
def post_pic(data, i):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']
###############################


def post_num_like(data):
    return data['node']['edge_liked_by']['count']


def post_preview_num_like(data):
    return data['node']['edge_media_preview_like']\
        ['count']


def post_edge_media_to_caption(data):
    return data['node']['edge_media_to_caption']['edges']


def post_edge_media_to_caption_text(data):
    return data['node']['edge_media_to_caption']['edges'][0]['node']['text']


def post_location(data):
    return data['node']['location']


def post_location_id(data):
    return data['id']


def post_location_has_public_page(data):
    return data['has_public_page']


def post_location_name(data):
    return data['name']


def post_location_slug(data):
    return data['slug']


def post_gating_info(data):
    return data['node']['gating_info']


def post_fact_check_overall_rating(data):
    return data['node']['fact_check_overall_rating']


def post_fact_check_information(data):
    return data['node']['fact_check_information']


def post_media_preview(data):
    return data['node']['media_preview']


def post_owner_id(data):
    return data['node']['owner']['id']


def post_owner_username(data):
    return data['node']['owner']['username']


def post_thumbnail_src(data):
    return data['node']['thumbnail_src']


def post_is_video(data):
    return data['node']['is_video']


def post_video_view_count(data, i):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['video_view_count']


def post_accessibility_caption(data):
    return data['node']['accessibility_caption']


def highlight_reel_count(data):
    return data['graphql']['user']['highlight_reel_count']


def logging_page_id(data):
    return data['logging_page_id']


def external_url(data):
    return data['graphql']['user']['external_url']


def external_url_linkshimmed(data):
    return data['graphql']['user']['external_url_linkshimmed']


def edge_mutual_followed_by_count(data):
    return data['graphql']['user']['edge_mutual_followed_by']['count']


def edge_saved_media_count(data):
    return data['graphql']['user']['edge_saved_media']['count']


def edge_saved_media_has_next_page(data):
    return data['graphql']['user']['edge_saved_media']['page_info']['has_next_page']


def edge_saved_media_end_cursor(data):
    return data['graphql']['user']['edge_saved_media']['page_info']['end_cursor']


def edge_media_collections_count(data):
    return data['graphql']['user']['edge_media_collections']['count']


def edge_media_collections_has_next_page(data):
    return data['graphql']['user']['edge_media_collections']['page_info']['has_next_page']


def edge_media_collections_end_cursor(data):
    return data['graphql']['user']['edge_media_collections']['page_info']['end_cursor']


def toast_content_on_load(data):
    return data['toast_content_on_load']


def shortcode_list(data):
    return data['node']['shortcode']


def shortcode_url(data):
    return data['node']['display_url']


def get_edges(data):
    return data['graphql']['user']['edge_owner_to_timeline_media']['edges']



