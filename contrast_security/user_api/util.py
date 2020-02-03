import base64
import validators


class Util:

    def __init__(self):
        pass

    @staticmethod
    def create_authorization_token(username, service_key):
        data_string = "{}:{}".format(username,service_key)
        data_bytes = data_string.encode("UTF-8")
        result = base64.b64encode(data_bytes)
        return result.decode('ascii')

    @staticmethod
    def validate_url(url):
        return validators.url(url)
