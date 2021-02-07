import requests
from config.test_data import *


class Token:
    """This class implements logic to generate auth tokens by calling REST API."""

    @staticmethod
    def generate_request_token():
        """Generate request token by calling REST API.

        Returns:
            Response object for request token generated.
        """
        request_token_response = requests.request("POST", url=f'{base_url}/auth/request_token', headers=token_headers, data=request_token_payload)
        return request_token_response

    @staticmethod
    def generate_access_token(request_token: str):
        """Generate access token by calling REST API.

        Returns:
            Response object for access token generated.
        """
        access_token_response = requests.request("POST", url=f'{base_url}/auth/access_token', headers=token_headers, data="{\"request_token\":\"%s\"}" % request_token)
        return access_token_response
