from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(
        max_length=512,
        widget=forms.Textarea(attrs={"rows": 6})
    )