# Chapa
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
    'tx_ref': '<your-unique-transation-id>',
    # optional
    'redirect_url': 'https://www.your-site.com/callback',
    'customization': {
        'title': '<Your-Company>',
        'description': 'Payment for your services',
    }
}

chapa = Chapa(api_key='<your_api_key>')
response = chapa.intialize(**data)
print(reponse['data']['checkout_url'])

# Another Implementation
chapa = Chapa(api_key='<your_api_key>', response_format='obj')
response = chapa.intialize(**data)
# notice how the response is an object
print(reponse.data.checkout_url)


# How to verify a transaction
response = chapa.verify('<your-unique-transation-id>')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. After that free to contribute to this project. Please Read the [CONTRIBUTING.md](https://github.com/chapimenge3/chapa) file for more information.

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
