import base64
import validators


class Util:

    def __init__(self):
        pass

    @staticmethod
    def create_authorization_token(username, service_key):
        return base64.standard_b64encode(username+':'+service_key)

    @staticmethod
    def validate_url(url):
        return validators.url(url)
