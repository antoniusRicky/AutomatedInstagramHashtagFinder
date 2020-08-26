import operator
from typing import Dict


# TODO
# non-latin character in hashtag
# blank caption
#


def retrieve_caption_from_post(post):
    print('hello world')


def retrieve_hashtag_from_caption(caption):
    print('hello world')


def filter_and_tally_hashtag(hashtags):
    final_hashtags: Dict[str, int] = {}  # final container; ready to show to user

    for hashtag in hashtags:
        if hashtag in final_hashtags:
            final_hashtags[hashtag] = final_hashtags[hashtag] + 1
        else:
            final_hashtags[hashtag] = 1

    return final_hashtags


def sort_final_hashtags(the_hashtags):
    the_hashtags = dict(sorted(the_hashtags.items(), key=operator.itemgetter(1), reverse=True))
    return the_hashtags


# TESTING, DELETE SOON
hashtags = ['hello', 'hello', 'world', 'hello', 'foo', 'bar', 'bar']
final_hashtags = filter_and_tally_hashtag(hashtags)
final_hashtags = sort_final_hashtags(final_hashtags)
print(final_hashtags)
