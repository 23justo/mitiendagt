from django import forms

from suppliers import models

class SupplierForm(forms.ModelForm):
    class Meta:
        model = models.Supplier
        fields = ('name','address','email','phone')