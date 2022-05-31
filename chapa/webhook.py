"""
Chapa Webhook API
"""
WEBHOOKS_EVENT_DESCRIPTION = {
    'charge.dispute.create': 'Dispute against company created.',
    'charge.dispute.remind': 'Reminder of an unresolved dispute against company.',
    'charge.dispute.resolve': 'Dispute has been resolved.',
    'charge.success': 'Charged successfully.',
    'customeridentification.failed': 'Customer identification failed.',
    'customeridentification.success': 'Customer identified successfully.',
    'invoice.create': 'An invoice has been created for a customer\'s subscription.'
    'Usually sent 3 days before the subscription is due.',
    'invoice.payment_failed': 'Payment for invoice has failed.',
    'invoice.update': 	'Customer\'s invoice has been updated. This invoice should'
    'be examined carfeully, and take necessary action.',
    'paymentrequest.pending': 	'Payment request has been sent to customer and payment is pending.',
    'paymentrequest.success': 	'Customer\'s payment is successful.',
    'subscription.create': 	'Subscription has been created.',
    'subscription.disable': 	'Account\'s subscription has been disabled.',
    'subscription.enable': 	'Account\'s subscription has been enabled.',
    'transfer.failed': 	'Transfer of money has failed.',
    'transfer.success': 	'A transfer has been completed.',
    'transfer.reversed': 	'A transfer has been reversed.',
    'issuingauthentication.request': 	'An authorization has been requested.',
    'issuingauthentication.created': 	'An authorization has been created.',
}

WEBHOOK_EVENT = WEBHOOKS_EVENT_DESCRIPTION.keys()
