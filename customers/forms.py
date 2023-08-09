from django import forms
from .models import CustomerModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'state']