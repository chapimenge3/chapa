"""
API SDK for Chapa Payment Gateway
"""
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-branches
# pylint: disable=too-many-arguments
import re
import json
import requests


class Response:
    """Custom Response class for SMS handling."""

    def __init__(self, dict1):
        self.__dict__.update(dict1)


class Chapa:
    """
    Simple SDK for Chapa Payment gateway
    """

    def __init__(self, secret, base_ur='https://api.chapa.co', api_version='v1',
                 response_format='json'):
        self._key = secret
        self.base_url = base_ur
        self.api_version = api_version
        if response_format and response_format in ['json', 'obj']:
            self.response_format = response_format
        else:
            raise ValueError('response_format must be \'json\' or \'obj\'')

        self.headers = {
            'Authorization': f'Bearer {self._key}'
        }

    def send_request(self, url, method, data=None, params=None, headers=None):
        """
        Request sender to the api

        Args:
            url (str): url for the request to be sent.
            method (str): the method for the request.
            data (dict, optional): request body. Defaults to None.

        Returns:
            response: response of the server.
        """
        if params and not isinstance(params, dict):
            raise ValueError("params must be a dict")

        if data and not isinstance(data, dict):
            raise ValueError("data must be a dict")

        if headers and isinstance(data, dict):
            headers.update(self.headers)
        elif headers and not isinstance(data, dict):
            raise ValueError("headers must be a dict")
        else:
            headers = self.headers

        func = getattr(requests, method)
        response = func(url, data=data, headers=headers)
        return getattr(response, "json", lambda: response.text)()

    def convert_response(self, response):
        """
        Convert Response data to a Response object

        Args:
            response (dict): The response data to convert

        Returns:
            Response: The converted response
        """
        if not isinstance(response, dict):
            return response

        return json.loads(json.dumps(response), object_hook=Response)

    def _construct_request(self, *args, **kwargs):
        """Construct the request to send to the API"""

        res = self.send_request(*args, **kwargs)
        if self.response_format == "obj" and isinstance(res, dict):
            return self.convert_response(res)

        return res

    def initialize(self, email: str, amount: int, first_name: str, last_name: str, tx_ref: str,
                   currency='ETB', callback_url=None, customization=None, headers=None):
        """
        Initialize the Transaction

        Args:
            email (str): customer email
            amount (int): amount to be paid
            first_name (str): first name of the customer
            last_name (str): last name of the customer
            tx_ref (str): your transaction id
            currency (str, optional): currency the transaction. Defaults to 'ETB'.
            callback_url (str, optional): url for the customer to redirect after payment.
                                          Defaults to None.
            customization (dict, optional): customization, currently 'title' and 'description'
                                            are available. Defaults to None.
            headers(dict, optional): header to attach on the request. Default to None

        Return:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'tx_ref': tx_ref,
            'currency': currency,
        }

        if not isinstance(amount, int):
            if str(amount).replace('.', '', 1).isdigit() and float(amount) > 0:
                pass
            else:
                raise ValueError("invalid amount")
        elif isinstance(amount, int):
            if amount < 0:
                raise ValueError("invalid amount")

        data['amount'] = amount

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("invalid email")

        data['email'] = email

        if callback_url:
            data['callback_url'] = callback_url

        if customization:
            if 'title' in customization:
                data['customization[title]'] = customization['title']
            if 'description' in customization:
                data['customization[description]'] = customization['description']
            if 'logo' in customization:
                data['customization[logo]'] = customization['logo']

        response = self._construct_request(
            url=f'{self.base_url}/{self.api_version}/transaction/initialize',
            method="post",
            data=data,
            headers=headers
        )
        return response

    def verify(self, transaction, headers=None):
        """Verify the transaction

        Args:
            transaction (str): transaction id

        Response:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """
        response = self._construct_request(
            url=f'{self.base_url}/{self.api_version}/transaction/verify/{transaction}',
            method="get",
            headers=headers
        )
        return response
