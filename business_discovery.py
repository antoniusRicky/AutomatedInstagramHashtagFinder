from defines import getCreds, makeApiCall


def getAccountInfo(params):
    """ Get info on a users account

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
    Returns:
        object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['fields'] = 'instagram_business_account.username(' + params[
        'ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}'  # string of fields to get back with the request for the account
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['page_id']  # endpoint url

    return makeApiCall(url, endpointParams, params['debug'])  # make the api call


params = getCreds()  # get creds
params['debug'] = 'yes'  # set debug
response = getAccountInfo(params)  # hit the api for some data!

print ("\n---- ACCOUNT INFO -----\n")  # display latest post info
print ("username:" ) # label
print (response['json_data']['instagram_business_account']['username'])  # display username
print ("\nnumber of posts:" ) # label
print (response['json_data']['instagram_business_account']['media_count'])  # display number of posts user has made
print ("\nfollowers:")  # label
print (response['json_data']['instagram_business_account']['followers_count'])  # display number of followers the user has
print ("\nfollowing:") # label
print (response['json_data']['instagram_business_account']['follows_count'])  # display number of people the user follows
print ("\nprofile picture url:")  # label
print (response['json_data']['instagram_business_account']['profile_picture_url'])  # display profile picutre url
print ("\nbiography:") # label
print (response['json_data']['instagram_business_account']['biography']) # display users about section