from chapa import Chapa
import random
import string

def generete_tx_ref(length):
    #Generate a transaction reference
    tx_ref = string.ascii_lowercase
    return ''.join(random.choice(tx_ref) for i in range(length))


def checkout():
	data = {
		# Required fields
		'email': 'user@example.com', # customer/client email address
		'amount': 1311.00, # total payment
		'first_name': 'Abebe', # customer/client first name
		'last_name': 'Bikila', # customer/client last name
		'tx_ref': generete_tx_ref(12),
		
		# Optional fields
		'callback_url': 'your_callback_url', # after successful payment chapa will redirect your customer/client to this url
		'customization': {
			'title': 'Example.com',
			'description': 'Payment for your services',
		}
	}

	chapa = Chapa('[YOUR_CHAPA_SECRET_KEY]')
	response = chapa.initialize(**data)

	# After successfull initialization redirect to the `checkout_url`
	if response['status'] == 'success':
		# do some action
		""" Redirect to the checkout page using `response['data']['checkout_url']` """
	else:
		# If initialization fails display the error message
		print(response['message'])
