# Chapa

[![Linter](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml/badge.svg)](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml)
[![Version](https://img.shields.io/static/v1?label=version&message=0.0.1&color=green)](https://travis-ci.com/chapimenge3/chapa)
[![Build](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml/badge.svg)](https://travis-ci.com/chapimenge3/chapa)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/licenses/mit)

Unofficial Python SDK for [Chapa API](https://developer.chapa.co/docs).

## Introduction

This document provides a comprehensive guide to integrating and using the Chapa Payment Gateway SDK in your application. Chapa is a powerful payment gateway that supports various payment methods, facilitating seamless transactions for businesses. This SDK simplifies interaction with Chapa’s API, enabling operations such as initiating payments, verifying transactions, and managing subaccounts.

## Installation

To use the Chapa SDK in your project, you need to install it using pip, as it is a dependency for making HTTP requests it will also install `httpx` as a dependency.

```bash
pip install chapa
```

## Usage

To begin using the SDK, import the `Chapa` class from the module and instantiate it with your secret key.

### Initializing the SDK

```python
from chapa import Chapa

# Replace 'your_secret_key' with your actual Chapa secret key
chapa = Chapa('your_secret_key')
```

### Async Support

The Chapa SDK implements async support using the `AsyncChapa` class. To use the async version of the SDK, import the `AsyncChapa` class from the module and instantiate it with your secret key.

```python
from chapa import AsyncChapa

# Replace 'your_secret_key' with your actual Chapa secret key
chapa = AsyncChapa('your_secret')
```

All of the below methods are available in the async version of the SDK. So you can just use it as you would use the sync version.

```python
response = await chapa.initialize(
    ...
)
```

### Making Payments

To initiate a payment, use the `initialize` method. This method requires a set of parameters like the customer's email, amount, first name, last name, and a transaction reference.

```python
response = chapa.initialize(
    email="customer@example.com",
    amount=1000,
    first_name="John",
    last_name="Doe",
    tx_ref="your_unique_transaction_reference",
    callback_url="https://yourcallback.url/here"
)
print(response)
```

### Verifying Payments

After initiating a payment, you can verify the transaction status using the `verify` method.

```python
transaction_id = "your_transaction_id"
verification_response = chapa.verify(transaction_id)
print(verification_response)
```

### Creating Subaccounts

You can create subaccounts for split payments using the `create_subaccount` method.

```python
subaccount_response = chapa.create_subaccount(
    business_name="My Business",
    account_name="My Business Account",
    bank_code="12345",
    account_number="0012345678",
    split_value="0.2",
    split_type="percentage"
)
print(subaccount_response)
```

### Bank Transfers

To initiate a bank transfer, use the `transfer_to_bank` method.

```python
transfer_response = chapa.transfer_to_bank(
    account_name="Recipient Name",
    account_number="0987654321",
    amount="500",
    reference="your_transfer_reference",
    bank_code="67890",
    currency="ETB"
)
print(transfer_response)
```

### Verifying Webhook

The reason for verifying a webhook is to ensure that the request is coming from Chapa. You can verify a webhook using the `verify_webhook` method.

```python
from chapa import verify_webhook

# request is just an example of a request object
# request.body is the request body
# request.headers.get("Chapa-Signature") is the Chapa-Signature header

verify_webhook(
    secret_key="your_secret_key",
    body=request.body,
    chapa_signature=request.headers.get("Chapa-Signature")
)
```

### Getting Testing Cards and Mobile Numbers

For testing purposes, you can retrieve a set of test cards and mobile numbers.

```python
from chapa import get_testing_cards, get_testing_mobile 

# Get a list of testing cards
test_cards = get_testing_cards()
print(test_cards)

# Get a list of testing mobile numbers
test_mobiles = get_testing_mobile()
print(test_mobiles)
```

### Get Webhook Events

You can get webhook events details with description like below

```python
from chapa import WEBHOOK_EVENTS, WEBHOOKS_EVENT_DESCRIPTION

# Get a list of webhook events
print(WEBHOOK_EVENTS)

# Get a list of webhook events with description
print(WEBHOOKS_EVENT_DESCRIPTION)
```

## Conclusion

The Chapa Payment Gateway SDK is a flexible tool that allows developers to integrate various payment functionalities into their applications easily. By following the steps outlined in this documentation, you can implement features like payment initialization, transaction verification, and sub-account management. Feel free to explore the SDK further to discover all the supported features and functionalities.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. After that free to contribute to this project. Please read the [CONTRIBUTING.md](https://github.com/chapimenge3/chapa/blob/main/CONTRIBUTING.md) file for more information.

Please make sure to update tests as appropriate.

## Run Locally

Clone the project

```bash
git clone https://github.com/chapimenge3/chapa.git
```

Go to the project directory

```bash
cd chapa
```

Install dependencies

```bash
pip install -r requirements.txt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Temkin Mengistu

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chapimenge.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chapimenge/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/chapimenge3/)
