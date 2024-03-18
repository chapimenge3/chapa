# API SDK for Chapa Payment Gateway Documentation

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

### Getting Testing Cards and Mobile Numbers

For testing purposes, you can retrieve a set of test cards and mobile numbers.

```python
# Get a list of testing cards
test_cards = chapa.get_testing_cards()
print(test_cards)

# Get a list of testing mobile numbers
test_mobiles = chapa.get_testing_mobile()
print(test_mobiles)
```

## Conclusion

The Chapa Payment Gateway SDK is a flexible tool that allows developers to integrate various payment functionalities into their applications easily. By following the steps outlined in this documentation, you can implement features like payment initialization, transaction verification, and subaccount management. Feel free to explore the SDK further to discover all the supported features and functionalities.
```
