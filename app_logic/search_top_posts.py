from app_logic.graph_api import get_credentials, make_api_call
import sys


def get_hashtag_info(params):
    endpoint_params = dict()  # container
    endpoint_params['user_id'] = params['instagram_user_id']
    endpoint_params['q'] = params['hashtag_name']
    endpoint_params['fields'] = 'id,name'
    endpoint_params['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'ig_hashtag_search'

    return make_api_call(url, endpoint_params, params['debug'])


def get_hashtag_media(params):
    endpoint_params = dict()
    endpoint_params['user_id'] = params['instagram_user_id']
    endpoint_params['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    endpoint_params['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

    return make_api_call(url, endpoint_params, params['debug'])


def get_top_posts(hashtag):
    params = get_credentials()
    params['hashtag_name'] = hashtag
    hashtag_info_response = get_hashtag_info(params)

    params['hashtag_id'] = hashtag_info_response['json_data']['data'][0]['id']

    print('Hashtag Info\n')
    print('Hashtag: ' + hashtag + '\n')
    print('Hashtag ID: ' + params['hashtag_id'] + '\n')

    print('Top Posts\n')
    params['type'] = 'top_media'
    hashtag_top_media_response = get_hashtag_media(params)

    post_number = 1
    for post in hashtag_top_media_response['json_data']['data']:
        print(' = POST #' + str(post_number) + '\n')
        post_number += 1

        print("Link to post:")
        print(post['permalink'] + '\n')

        print("Post caption:")
        print(post['caption'] + '\n')

        print("Media type:")
        print(post['media_type'] + '\n\n')
