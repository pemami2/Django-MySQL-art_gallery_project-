from django import forms

class NameForm(forms.Form): 
    category = forms.CharField()
    sort = forms.CharField()
    post = forms.CharField()