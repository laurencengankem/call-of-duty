from app.parser import profiling
from datetime import datetime
import pytz

comment_text = []


def get_comment_data(comment):
    global comment_text 
    comment_has_next_page            = profiling.get_comment_has_next_page(comment)
    profiling.comment_for_function(comment)
    list_comment_id                  = profiling.get_comment_id()                   
    comment_text                     = profiling.get_comment_text()
    comment_created_at               = profiling.get_comment_created_at()
    comment_owner_id                 = profiling.get_comment_owner_id()
    comment_owner_username           = profiling.get_comment_owner_username()
    comment_found_tag                = profiling.comment_found_tag()
    comment_found_hashtag            = profiling.comment_found_hashtag()

    context_comment = {
        'shortcode': comment['shortcode'],
        'date_time': datetime.now(tz=pytz.timezone('Europe/Rome')),
        'list_comment_id': list_comment_id,
        'comment_text': comment_text,
        'comment_created_at': comment_created_at,
        'comment_owner_id': comment_owner_id,
        'comment_owner_username': comment_owner_username,
        'comment_found_tag': comment_found_tag,
        'comment_found_hashtag': comment_found_hashtag,
    }
    return context_comment

def get_comment_text():
    return comment_text