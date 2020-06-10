from app import endpoint
from app.request_handler import send_requests
from app.request_handler import request_adapter as rq
from app import json_parser as parser
import pika
import json
import requests

'''
    This function sends requests to Instagram API and return in the task queue the downloaded json
'''
def request_to_username(username):
    profile_name = username

    url = endpoint.request_account_info(profile_name)

    if send_requests.is_requested:

        message = rq.user_request(url)

        if message is not None:
            try:
                user_id = parser.id_number(message)
            except KeyError as e:
                click.secho(
                    " [start.py>user-id]\tUnable to get user ID. %s. Check if the username is correct.\n" %e,
                    fg="green",
                    )
            r=requests.post("http://127.0.0.1:5002/", json=message)
            print(r.status_code)
            try:

                is_private = parser.is_private(message)
                if not is_private:

                    count_post = 0
                    for post in parser.shortcode(message):

                        shortcode = post['node']['shortcode']
                        comment = rq.comment_media_request(endpoint.request_comment(shortcode, ''))
                        end_cursor = parser.end_cursor_comment(comment)
                        comment['shortcode'] = shortcode
                        r= requests.post("http://127.0.0.1:5002/", json=comment)
                        count_end_cursor = 0

                        while not end_cursor is None:
                            count_end_cursor += 1
                            if count_end_cursor == 3:
                                break
                            comment = rq.comment_media_request(endpoint.request_comment(shortcode, end_cursor))
                            end_cursor = parser.end_cursor_comment(comment)
                            comment['shortcode'] = shortcode
                            r= requests.post("http://127.0.0.1:5002/", json=comment)
                        print(" [x] Sent %r" % "COMMENT JSON N. "+str(count_end_cursor))
            except KeyError as e:
                click.secho(
                    " [start.py>private]\tUnable to check if user is private. %s. Check if the username is correct.\n" %e,
                    fg="green",
                    )

    return message
