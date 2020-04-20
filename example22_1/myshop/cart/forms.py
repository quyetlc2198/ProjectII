from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 20)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField( choices=PRODUCT_QUANTITY_CHOICES,coerce=int,initial=1)
    update = forms.BooleanField(required=False,initial=False, widget=forms.HiddenInput)
    widgets = {
        'quantity' : forms.Select(attrs={'class' : 'btn_quantity'},)
    }
