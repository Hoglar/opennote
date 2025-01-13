from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(max_length=32)
    category = forms.CharField(
        max_length=32,
        label="Category:",
        widget=forms.TextInput(attrs={'list': 'categories', "spellcheck": "false"})
        )
    note = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 16}),
    )

class OverviewFilter(forms.Form):
    author = forms.CharField(max_length=32, required=False)
    category = forms.CharField(max_length=64, required=False)
    search = forms.CharField(max_length=64, required=False)
    TIME_PERIOD_CHOICES = [
        ('all', 'All'),
        ('1_month', '1 Month'),
        ('3_months', '3 Months'),
        ('1_year', '1 Year'),
    ]
    time_period = forms.ChoiceField(choices=TIME_PERIOD_CHOICES, required=False, initial='all')

class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=512,
        widget=forms.Textarea(attrs={"rows": 3})
    )

class HelpDescriptionForm(forms.Form):
    description = forms.CharField(
        max_length=256,
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False

    )
    offer = forms.ChoiceField(
        choices=[("Help", "Help"), ("None", "None")],
        widget=forms.RadioSelect,
        required=False
    )