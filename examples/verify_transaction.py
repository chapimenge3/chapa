from chapa import Chapa


def verify(transaction_id):
	""" Accept the transaction id and verify it """
	chapa = Chapa('[YOUR_CHAPA_SECRET_KEY]')
	response = chapa.verify(transaction_id)

	if response['status'] == 'success':
		# do some actions, probably redirect to success page
		pass
	else:
		# do some actions, probably redirect to failed page
		pass

	"""
	If verification response has succeed it looks like
		{'message': 'Payment details', 'status': 'success', 'data': {
		'first_name': 'Abebe', 'last_name': 'Bikila', 'email': 'user@example.com', 'currency': 'ETB', 
		'amount': '1,311.00', 'charge': '45.89', 'mode': 'test', 'method': 'test', 'type': 'API', 
		'status': 'success', 'reference': '[reference]', 'tx_ref': '[tx_ref]', 
		'customization': {'title': 'Example.com', 'description': 'Payment for your services', 'logo': None}, 
		'meta': None, 'created_at': '2022-08-24T12:29:52.000000Z', 'updated_at': '2022-08-24T12:29:52.000000Z'}}
	"""
