from django import forms
from bangazon_webstore.models.paymenttypes import PaymentType
from bangazon_webstore.models.product_model import Product
from django.utils.translation import ugettext_lazy as _

class PaymentTypeForm(forms.ModelForm):

	class Meta:
		model = PaymentType
		help_texts = {
			'card_type': _('Card Type:'),
			'card_number': _('Card Number:'),
			'cvv': _('3 digit cvv '),
			'expiration': _('Exp. Date:'),
			'name_on_card': _('Full Name on Card:')
		}
		fields = ('card_type', 'card_number', 'cvv', 'expiration', 'name_on_card')


class SellProductForm(forms.ModelForm):

	class Meta:
		model = Product
		help_texts = {
			'name': _('Product Name:'),
			'description': _('Describe your Product:'),
			'price': _('Price:'),
			'quantity': _('Stock:'),
			'product_type': _('Choose Category:')
		}
		fields = ('name', 'description', 'price', 'quantity', 'product_type')

