from django import forms


class PlayerSignUpForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    zipcode = forms.CharField()
    state = forms.CharField()
    country = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()

