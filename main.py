import tweepy


# Auth:

def auth_twitter(api_key, api_secret_key, access_tok, access_tok_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)

    auth.set_access_token(access_tok, access_tok_secret)

    return auth


auth = auth_twitter('09nFtECOjaCCvL3JQjJcxvVLt', 'MplwsC879nCoFffxwXP1oWRRfD4l990ZK0o2tuE4mty9rXxS5N',
                    '1277383591014563840-ZJNhopLOEajbdwq0k8wc6fmqSyST1Y',
                    'cGsbRZzZOB0lM6AY24774DaxBlrTgVA6KSakp1qmr8EWn')

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


# Make Retweets:

def make_ret(api_ref, keyword, n):
    for i in api_ref.search(q=keyword, count=n):
        api_ref.retweet(i.id)


make_ret(api, '#deeplearning', 1)
