# Chapa

[![Linter](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml/badge.svg)](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml)
[![Version](https://img.shields.io/static/v1?label=version&message=0.0.1&color=green)](https://travis-ci.com/chapimenge3/chapa)
[![Build](https://github.com/chapimenge3/chapa/actions/workflows/Linter.yml/badge.svg)](https://travis-ci.com/chapimenge3/chapa)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/licenses/mit)

Unofficial Python SDK for [Chapa API](https://developer.chapa.co/docs).

## Instructions

This is a Python SDK for Chapa API. It is not official and is not supported by Chapa. It is provided as-is. Anyone can contribute to this project.

## Installation

```
pip install chapa
```

## Usage

```python
from chapa import Chapa

data = {
    'email': 'abebe@bikila.com',
    'amount': 1000,
    'first_name': 'Abebe',
    'last_name': 'Bikila',
    'tx_ref': '<your-unique-transaction-id>',
    # optional
    'callback_url': 'https://www.your-site.com/callback',
    'customization': {
        'title': '<Your-Company>',
        'description': 'Payment for your services',
    }
}

chapa = Chapa('<your_api_key>')
response = chapa.initialize(**data)
print(response['data']['checkout_url'])

# Another Implementation
chapa = Chapa('<your_api_key>', response_format='obj')
response = chapa.initialize(**data)
# notice how the response is an object
print(response.data.checkout_url)


# How to verify a transaction
response = chapa.verify('<your-unique-transaction-id>')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. After that free to contribute to this project. Please read the [CONTRIBUTING.md](https://github.com/chapimenge3/chapa/blob/main/CONTRIBUTING.md) file for more information.

Please make sure to update tests as appropriate.

## API Reference

### Create new Transaction

Base endpoint https://api.chapa.co/v1

```http
  POST /transaction/initialize
```

| Parameter               | Type      | Description                                                                                                                                                                                        |
| :---------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                   | `string`  | **Required**. This will be your public key from Chapa. When on test mode use the test key, and when on live mode use the live key.                                                                 |
| `email`                 | `string`  | **Required**. A customer’s email. address                                                                                                                                                          |
| `amount`                | `integer` | **Required**. The amount you will be charging your customer.                                                                                                                                       |
| `first_name`            | `string`  | **Required**. Your API key                                                                                                                                                                         |
| `last_name`             | `string`  | **Required**. A customer’s last name.                                                                                                                                                              |
| `tx_ref`                | `string`  | **Required**. A unique reference given to each transaction.                                                                                                                                        |
| `currency`              | `string`  | **Required**. The currency in which all the charges are made. Currency allowed is ETB.                                                                                                             |
| `callback_url`          | `string`  | The URL to redirect the customer to after payment is done.                                                                                                                                         |
| `customization[title]` | `string`  | The customizations field (optional) allows you to customize the look and feel of the payment modal. You can set a logo, the store name to be displayed (title), and a description for the payment. |

| HEADER Key      | Value                   |
| :-------------- | :---------------------- |
| `Authorization` | `Bearer <YOUR-API-KEY>` |

### Verify Transaction

```http
  GET /transaction/verify/${tx_ref}
```

| Parameter | Type     | Description                                                |
| :-------- | :------- | :--------------------------------------------------------- |
| `tx_ref`  | `string` | **Required**. A unique reference given to each transaction |

## FAQ

#### No Available Questions!

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
