from django import forms
from .models import Profile

from core.forms.fields import PhoneNumberField
from core.forms.widgets import PhoneNumberInput, DatePickerInput

class ProfileForm(forms.ModelForm):
    # phone_number = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address"].required = True

    class Meta:
        model = Profile
        fields = [
            "birth_date",
            "address",
            "phone_number",
            "photo",
        ]
        widgets = {
            "birth_date": DatePickerInput,
            "phone_number": PhoneNumberInput,
        }