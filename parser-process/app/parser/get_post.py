from app.parser import profiling
from datetime import datetime
import pytz


def get_post_data(info):
    post_count                         = profiling.post_get_post_count(info)
    post_page_info_has_next_page       = profiling.post_get_post_page_info_has_next_page(info)
    post_page_info_end_cursor          = profiling.post_get_post_page_info_end_cursor(info)
    edges                              = profiling.post_get_post_edges(info)

    if edges:
        post_text = profiling.post_get_post_text(info)
        profiling.post_for_function(info)
        post_id                        = profiling.post_get_post_id()
        post_typename                  = profiling.post_get_post_typename()
        post_shortcode                 = profiling.post_get_post_edge_media_to_caption_shortcode()
        post_comment_count             = profiling.post_get_post_edge_media_to_comment_count()
        post_comment_disabled          = profiling.post_get_post_comment_disabled()
        post_taken_at_timestamp        = profiling.post_get_post_taken_at_timestamp()
        post_width, post_height        = profiling.post_get_post_dimensions()
        post_display_url               = profiling.post_get_post_display_url()
        post_preview_like_count        = profiling.post_get_post_preview_like_count()
        post_hashtag                   = profiling.post_get_post_hashtag()
        post_tag                       = profiling.post_get_post_tag()
        post_owner_id                  = profiling.post_get_post_owner_id()
        post_thumbnail_src             = profiling.post_get_list_post_thumbnail_src()
        post_is_video                  = profiling.post_get_post_is_video()
        post_video_view_count          = profiling.post_get_post_video_view_count()


    post_context = {
        'post_count':                   post_count,
        'date_time':                    datetime.now(tz=pytz.timezone('Europe/Rome')),
        'post_id':                      post_id,
        'post_typename':                post_typename,
        'post_text':                    post_text,
        'post_shortcode':               post_shortcode,
        'post_comment_count':           post_comment_count,
        'post_comment_disabled':        post_comment_disabled,
        'post_taken_at_timestamp':      post_taken_at_timestamp,
        'post_dimension_width':         post_width,
        'post_dimension_height':        post_height,
        'post_display_url':             post_display_url,
        'post_preview_like_count':      post_preview_like_count,
        'post_hashtag':                 post_hashtag,
        'post_tag':                     post_tag,
        'post_owner_id':                post_owner_id,
        'post_thumbnail_src':           post_thumbnail_src,
        'post_is_video':                post_is_video,
        'post_video_view_count':        post_video_view_count

    }
    return post_context