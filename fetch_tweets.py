import requests
from authentication import Authentication

class Recent_Search:
    """
    Search Tweets: GET /2/tweets/search/recent
    https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
    """

    def __init__(self):
        """
        :param authentication: Authentication object (see authentication.py)
        :param max_results: The maximum number of search results to be returned by a request. Has to be between 10 and 100.
        """
        
        self.url = "https://api.twitter.com/2/tweets/search/recent?tweet.fields=id,text,attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,withheld&expansions=author_id,referenced_tweets.id,in_reply_to_user_id,attachments.media_keys,attachments.poll_ids,geo.place_id,entities.mentions.username,referenced_tweets.id.author_id&media.fields=media_key,type,duration_ms,height,preview_image_url,url,public_metrics,width,alt_text&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type&poll.fields=duration_minutes,end_datetime,id,options,voting_status&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld"
        self.auth = Authentication()
        self.headers = {"Content-Type": "application/json"}
    
    def __call__(self, query_parameters):
        """
        :param query_parameters: dict
        :return: Response payload containing results that match query and timeframe
        """

        return requests.request(
            "GET",
            url = self.url,
            params = query_parameters,
            headers = self.headers,
            auth = self.auth.get_oauth2_bearer_token
        )