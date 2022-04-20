import os

class Authentication:
    """
    Class to handle authentication for the Twitter API
    """

    def __init__(self):
        self.BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    
    def get_oauth2_bearer_token(self, r):
        
        r.headers["Authorization"] = f"Bearer {self.BEARER_TOKEN}"
        return r

