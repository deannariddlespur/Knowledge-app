from django import forms
from .models import Result


class ResultForm(forms.ModelForm):
    CHOICES = (
        (False, "False"),
        (True, "True")
    )
    result = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="")

    class Meta:
        model = Result
        fields = ["result"]
