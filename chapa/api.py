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


def convert_response(response):
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


class Chapa:
    """
    Simple SDK for Chapa Payment gateway
    """

    def __init__(
        self,
        secret,
        base_ur="https://api.chapa.co",
        api_version="v1",
        response_format="json",
    ):
        self._key = secret
        self.base_url = base_ur
        self.api_version = api_version
        if response_format and response_format in ["json", "obj"]:
            self.response_format = response_format
        else:
            raise ValueError("response_format must be 'json' or 'obj'")

        self.headers = {"Authorization": f"Bearer {self._key}"}

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

    def _construct_request(self, *args, **kwargs):
        """Construct the request to send to the API"""

        res = self.send_request(*args, **kwargs)
        if self.response_format == "obj" and isinstance(res, dict):
            return convert_response(res)

        return res

    def initialize(
        self,
        email: str,
        amount: int,
        first_name: str,
        last_name: str,
        tx_ref: str,
        currency="ETB",
        phone_number=None,
        callback_url=None,
        return_url=None,
        customization=None,
        headers=None,
        **kwargs,
    ):
        """
        Initialize the Transaction

        Args:
            email (str): customer email
            amount (int): amount to be paid
            first_name (str): first name of the customer
            last_name (str): last name of the customer
            tx_ref (str): your transaction id
            phone_number (str, optional): phone number of the customer.
                                          Defaults to None.
            currency (str, optional): currency the transaction. Defaults to 'ETB'.
            callback_url (str, optional): function that runs when payment is successful.
                                          Defaults to None.
            return_url (str, optional): web address to redirect the user after payment is
                                        successful. Defaults to None.
            customization (dict, optional): customization, currently 'title' and 'description'
                                            are available. Defaults to None.
            headers(dict, optional): header to attach on the request. Default to None

        Return:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "tx_ref": tx_ref,
            "currency": currency,
        }

        if kwargs:
            data.update(kwargs)

        if not isinstance(amount, int):
            if str(amount).replace(".", "", 1).isdigit() and float(amount) > 0:
                pass
            else:
                raise ValueError("invalid amount")
        elif isinstance(amount, int):
            if amount < 0:
                raise ValueError("invalid amount")

        data["amount"] = amount

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("invalid email")

        data["email"] = email

        if phone_number:
            data["phone_number"] = phone_number

        if callback_url:
            data["callback_url"] = callback_url

        if return_url:
            data["return_url"] = return_url

        if customization:
            if "title" in customization:
                data["customization[title]"] = customization["title"]
            if "description" in customization:
                data["customization[description]"] = customization["description"]
            if "logo" in customization:
                data["customization[logo]"] = customization["logo"]

        response = self._construct_request(
            url=f"{self.base_url}/{self.api_version}/transaction/initialize",
            method="post",
            data=data,
            headers=headers,
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
            url=f"{self.base_url}/{self.api_version}/transaction/verify/{transaction}",
            method="get",
            headers=headers,
        )
        return response

    def create_subaccount(self, business_name: str, account_name: str, bank_code: str,
                          account_number: str, split_value: str, split_type: str,
                          headers=None, **kwargs):
        """
        Create a subaccount for split payment

        Args:
            business_name (str): business name
            account_name (str): account name
            bank_code (str): bank code
            account_number (str): account number
            split_value (str): split value
            split_type (str): split type
            headers(dict, optional): header to attach on the request. Default to None
            **kwargs: additional data to be sent to the server

        Return:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """

        data = {
            'business_name': business_name,
            'account_name': account_name,
            'bank_code': bank_code,
            'account_number': account_number,
            'split_value': split_value,
            'split_type': split_type,
        }

        if kwargs:
            data.update(kwargs)

        response = self._construct_request(
            url=f'{self.base_url}/{self.api_version}/subaccount',
            method="post",
            data=data,
            headers=headers
        )
        return response

    def initialize_split_payment(self, amount: int, currency: str, email: str, first_name: str,
                                 last_name: str, tx_ref: str, callback_url: str, return_url: str,
                                 subaccount_id: str, headers=None, **kwargs):
        """
        Initialize split payment transaction

        Args:
            email (str): customer email
            amount (int): amount to be paid
            first_name (str): first name of the customer
            last_name (str): last name of the customer
            tx_ref (str): your transaction id
            currency (str, optional): currency the transaction. Defaults to 'ETB'.
            callback_url (str, optional): url for the customer to redirect after payment.
                                          Defaults to None.
            return_url (str, optional): url for the customer to redirect after payment.
                                          Defaults to None.
            subaccount_id (str, optional): subaccount id to split payment.
                                          Defaults to None.
            headers(dict, optional): header to attach on the request. Default to None
            **kwargs: additional data to be sent to the server

        Return:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'tx_ref': tx_ref,
            'currency': currency,
            'callback_url': callback_url,
            'return_url': return_url,
            'subaccount_id': subaccount_id
        }

        if kwargs:
            data.update(kwargs)

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

        response = self._construct_request(
            url=f'{self.base_url}/{self.api_version}/transaction/initialize',
            method="post",
            data=data,
            headers=headers
        )
        return response

    def get_banks(self, headers=None):
        """Get the list of all banks

        Response:
            dict: response from the server
            response(Response): response object of the response data return from the Chapa server.
        """
        response = self._construct_request(
            url=f"{self.base_url}/{self.api_version}/banks",
            method="get",
            headers=headers,
        )
        return response
