from django import forms
from .models import Order
from product.models import Product
from kuser.models import Kuser
from django.db import transaction


class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입력해주세요.'
        },
        label='상품설명', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')

        if not(quantity and product):
            if quantity is None:
                self.add_error('quantity', '값이 없습니다.')
            if product is None:
                self.add_error('product', '값이 없습니다.')
