from django import forms

from .models import Subscriber


class SubscriberAddForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'})
    )

    class Meta:
        model = Subscriber
        fields = ('email','first_name', 'last_name',)

