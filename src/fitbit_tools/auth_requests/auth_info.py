class AuthInfo:
    def __init__(self, access_token, expires_at, refresh_token, user_id):
        self.access_token = access_token
        self.expires_at = expires_at
        self.refresh_token = refresh_token
        self.user_id = user_id
