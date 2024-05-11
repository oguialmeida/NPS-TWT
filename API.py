import requests

class SocialMediaAPIClient:
    def __init__(self, api_key, session="", proxy=""):
        self.api_key = api_key
        self.base_url = "https://socialmediaapi.p.rapidapi.com/"
        self.social_session = session
        self.social_proxy = proxy

    def _get_headers(self):
        return {
            "social-session": self.social_session,
            "social-proxy": self.social_proxy,
            "x-rapidapi-host": "socialmediaapi.p.rapidapi.com",
            "x-rapidapi-key": self.api_key,
            "content-type": "application/json",
        }

    def _send_request(self, method, endpoint, params=None, data=None):
        url = self.base_url + endpoint
        headers = self._get_headers()

        if method == "POST":
            headers["content-type"] = "application/x-www-form-urlencoded"
            
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()

        return response.json()
    
    def get_post(self, post_id):
        endpoint = "get-post"
        params = {
            "post_id": post_id
        }
        return self._send_request("GET", endpoint, params)

    def get_post_comments(self, post_id):
        endpoint = "get-post-comments"
        params = {
            "post_id": post_id
        }
        return self._send_request("GET", endpoint, params)
    
    def user_posts(self, username=None, user_id=None, cursor=None):
        endpoint = "user-posts"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def user_media(self, username=None, user_id=None, cursor=None):
        endpoint = "user-media"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def user_likes(self, username=None, user_id=None, cursor=None):
        endpoint = "user-likes"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def explore_timeline(self, cursor=None):
        endpoint = "explore-timeline"
        params = {
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def following_timeline(self, cursor=None):
        endpoint = "following-timeline"
        params = {
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def create_post(self, post_text, attachment_url=None, in_reply_to_post_id=None, media_id=None):
        endpoint = "create-post"
        data = {
            "post_text": post_text,
            "attachment_url": attachment_url,
            "in_reply_to_post_id": in_reply_to_post_id,
            "media_id": media_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def delete_post(self, post_id):
        endpoint = "delete-post"
        params = {
            "post_id": post_id
        }
        return self._send_request("GET", endpoint, params)
    
    def get_user(self, username=None):
        endpoint = "get-user"
        params = {
            "username": username
        }
        return self._send_request("GET", endpoint, params)
    
    def user_followers(self, username=None, user_id=None, cursor=None):
        endpoint = "user-followers"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def user_following(self, username=None, user_id=None, cursor=None):
        endpoint = "user-following"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_suggestions(self, query, cursor=None):
        endpoint = "search-suggestions"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_top(self, query, cursor=None):
        endpoint = "search-top"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_latest(self, query, cursor=None):
        endpoint = "search-latest"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_users(self, query, cursor=None):
        endpoint = "search-users"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_images(self, query, cursor=None):
        endpoint = "search-images"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def search_videos(self, query, cursor=None):
        endpoint = "search-videos"
        params = {
            "query": query,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def login_email_username(self, username_or_email, password):
        endpoint = "login-email-username"
        data = {
            "username_or_email": username_or_email,
            "password": password
        }
        return self._send_request("POST", endpoint, data=data)
    
    def login_2fa(self, login_data, response):
        endpoint = "login-2fa"
        data = {
            "login_data": login_data,
            "response": response
        }
        return self._send_request("POST", endpoint, data=data)
    
    def logout(self):
        endpoint = "logout"
        return self._send_request("POST", endpoint)
    
    def follow_user(self, username=None, user_id=None):
        endpoint = "follow-user"
        data = {
            "username": username,
            "user_id": user_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def unfollow_user(self, username=None, user_id=None):
        endpoint = "unfollow-user"
        data = {
            "username": username,
            "user_id": user_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def like_post(self, post_id):
        endpoint = "like-post"
        data = {
            "post_id": post_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def unlike_post(self, post_id):
        endpoint = "unlike-post"
        data = {
            "post_id": post_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def share_post(self, post_id):
        endpoint = "share-post"
        data = {
            "post_id": post_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def unshare_post(self, post_id):
        endpoint = "unshare-post"
        data = {
            "post_id": post_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def get_message_conversations(self, cursor=None):
        endpoint = "get-message-conversations"
        params = {
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def get_message_conversation(self, username=None, user_id=None, cursor=None):
        endpoint = "get-message-conversation"
        params = {
            "username": username,
            "user_id": user_id,
            "cursor": cursor
        }
        return self._send_request("GET", endpoint, params)
    
    def send_message(self, message, to_user_name=None, to_user_id=None, media_id=None):
        endpoint = "send-message"
        data = {
            "message": message,
            "to_user_name": to_user_name,
            "to_user_id": to_user_id,
            "media_id": media_id
        }
        return self._send_request("POST", endpoint, data=data)
    
    def upload_image(self, image_url):
        endpoint = "upload-image"
        data = {
            "image_url": image_url
        }
        return self._send_request("POST", endpoint, data=data)
