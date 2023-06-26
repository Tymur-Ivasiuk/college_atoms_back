from django import forms


class ZvitForm(forms.Form):
    date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date'})
    )
    executor = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Executor'})
    )
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )