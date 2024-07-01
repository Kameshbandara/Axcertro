from django import forms

from .models import details


class detailForm(forms.ModelForm):
    class Meta:
        model = details
        fields = ['First_Name', 'Last_Name', 'Email']