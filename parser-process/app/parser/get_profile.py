from app.parser import profiling, json_parser
from datetime import datetime
from app.parser import get_popular_hashtag
from app.parser import get_popular_tag
from app.parser import get_max_likes_hashtag
import pytz

def get_user_data(info):

    '''
    This function has the responsibility to query the JSON received from the Instagram API asking for the required field
    that we want to insert in the "final JSON", the one who will be inserted into the db

    :param info:    JSON to be analyzed
    :return:        JSON that only containes the required field for rendering the HTML page
    '''

    bio                                     = json_parser.biography(info)
    blocked_by_viewer                       = json_parser.blocked_by_viewer(info)
    business                                = json_parser.is_business(info)
    connected_fb_page                       = json_parser.connected_fb_page(info)
    country_block                           = json_parser.country_block(info)
    cursor                                  = ''
    edge_media_collections_count            = json_parser.edge_media_collections_count(info)
    edge_media_collections_end_cursor       = json_parser.edge_media_collections_end_cursor(info)
    edge_media_collections_has_next_page    = json_parser.edge_media_collections_has_next_page(info)
    edge_saved_media_end_cursor             = json_parser.edge_saved_media_end_cursor(info)
    edge_saved_media_has_next_page          = json_parser.edge_saved_media_has_next_page(info)
    external_url                            = json_parser.external_url(info)
    external_url_linkshimmed                = json_parser.external_url_linkshimmed(info)
    followed_by_viewer                      = json_parser.followed_by_viewer(info)
    follows_viewer                          = json_parser.follows_viewer(info)
    fullname                                = json_parser.fullname(info)
    has_blocked_viewer                      = json_parser.has_blocked_viewer(info)
    has_channel                             = json_parser.has_channel(info)
    has_requested_viewer                    = json_parser.has_requested_viewer(info)
    id                                      = json_parser.id_number(info)
    joined_recently                         = json_parser.is_joined_recently(info)
    list_of_url                             = ['']
    logging_page_id                         = json_parser.logging_page_id(info)
    no_edge_mutual_followed_by              = json_parser.edge_mutual_followed_by_count(info)
    no_edge_saved_media                     = json_parser.edge_saved_media_count(info)
    no_followers                            = json_parser.followers(info)
    no_following                            = json_parser.following(info)
    no_highlight_reel                       = json_parser.highlight_reel_count(info)
    no_posts                                = json_parser.post_number(info)
    post_preview                            = 0
    private                                 = json_parser.is_private(info)
    requested_by_viewer                     = json_parser.requested_by_viewer(info)
    url                                     = json_parser.profile_pic(info)
    toast_content_on_load                   = json_parser.toast_content_on_load(info)
    username                                = json_parser.username(info)
    verified                                = json_parser.is_verified(info)
#   profiling.get_show_suggested_profiles(info)

    '''
        The fields above are always present in the JSON even if the profile is private. Instead, the following fields 
        may be present, only if the profile is public
    '''
    overall_timestamp      = []
    timestamp              = []
    postInfo               = []
    post_tag               = []
    post_hashtag           = []
    popular_hashtag        = []
    popular_tag            = []
    max_likes_hashtag      = []
    max_comments_hashtag   = []
    cross_common_hashtag   = []
    likes_and_comments     = []
    datepost               = []
    accessibility_caption  = []
    photo_description      = []
    if private is False:
        profiling.loadLists(info)
        list_of_shortcode, list_of_url                = profiling.get_shortcode_list()
        # postinfo 0 shortcode, 1 url, 2 number of like, 3 comments
        postInfo                                      = profiling.get_postInfo()
        post_type_name                                = profiling.get_post_type_name()
        post_id                                       = profiling.get_post_id()
        post_comment_count                            = profiling.get_post_comment_count()
        post_comments_disabled                        = profiling.get_post_comments_disabled()
        post_taken_at_timestamp                       = profiling.get_post_taken_at_timestamp()
        post_dimensions_height, post_dimensions_width = profiling.get_post_dimensions()
        post_edge_media_to_caption_text               = profiling.get_post_text()
        locations                                     = profiling.get_post_location()
        post_location_id                              = []
        post_location_has_public_page                 = []
        post_location_name                            = []
        post_location_slug                            = []
        for location in locations:
            if location is None:
                post_location_id.append(" ")
                post_location_has_public_page.append(" ")
                post_location_name.append(" ")
                post_location_slug.append(" ")
            else:
                post_location_id.append(json_parser.post_location_id(location))
                post_location_has_public_page.append(json_parser.post_location_has_public_page(location))
                post_location_name.append(json_parser.post_location_name(location))
                post_location_slug.append(json_parser.post_location_slug(location))
        is_video                                      = profiling.get_post_is_video()
        video_view_count                              = []
        post_accessibility                            = []
        post_num_like, post_preview_num_like          = profiling.get_post_like()
        post_owner_id, post_owner_username            = profiling.get_post_owner()
        post_media_preview                            = []
        post_preview                                  = json_parser.post_number(info)
        for edge in json_parser.get_edges(info):
            accessibility_caption.append(json_parser.post_accessibility_caption(edge))
            post_media_preview.append(json_parser.post_media_preview(edge))
        post_gating_info, post_fact_check_overall_rating, \
            post_fact_check_information              = profiling.get_post_data2()
            
        post_hashtag                                 = profiling.post_found_hashtag()
        post_tag                                     = profiling.post_found_tag()
        overall_timestamp, timestamp                 = profiling.get_timestamp()
        datepost                                     = profiling.get_dateLike()
        popular_hashtag                              = get_popular_hashtag.get_hashtag(post_hashtag)
        popular_tag                                  = get_popular_tag.get_tag(post_tag)
        max_likes_hashtag                            = get_max_likes_hashtag.get_max_likes(postInfo, post_hashtag)
        max_comments_hashtag                         = get_max_likes_hashtag.get_max_comments(postInfo, post_hashtag)
        cross_common_hashtag                         = get_max_likes_hashtag.get_common_hashtag(postInfo, post_hashtag)
        likes_and_comments                           = get_max_likes_hashtag.get_likes_comments(postInfo)
        photo_description                            = get_max_likes_hashtag.get_photo_description(accessibility_caption)

    context = {
        'date_time':                datetime.now(),
        'username':                 username,
        'fullname':                 fullname,
        'id':                       id,
        'url':                      url,
        'bio':                      bio,
        'post_preview':             post_preview,
        'n_followers':              no_followers,
        'n_following':              no_following,
        'n_post':                   no_posts,
        'cursor':                   cursor,
        'verified':                 verified,
        'business':                 business,
        'private':                  private,
        'blocked_by_viewer':        blocked_by_viewer,
        'country_block':            country_block,
        'followed_by_viewer':       followed_by_viewer,
        'follows_viewer':           follows_viewer,
        'has_channel':              has_channel,
        'has_blocked_viewer':       has_blocked_viewer,
        'has_requested_viewer':     has_requested_viewer,
        'joined_recently':          joined_recently,
        'requested_by_viewer':      requested_by_viewer,
        'connected_fb_page':        connected_fb_page,
        'list_url_post':            list_of_url,
        'overall_timestamp':        overall_timestamp,
        'timestamp':                timestamp,
        'shortcode_url':            postInfo, 
        'hashtag':                  post_hashtag,
        'tag':                      post_tag,
        'popular_hashtag':          popular_hashtag,
        'popular_tag':              popular_tag,
        'max_likes_hashtag':        max_likes_hashtag,
        'max_comments_hashtag':     max_comments_hashtag,
        'cross_common_hashtag':     cross_common_hashtag,
        'likes_and_comments':       likes_and_comments,
        'post_timestamp':           datepost,
        'photo_description':        photo_description,
        #'post_timestamp':           datepost[::-1],

    }
    return context
