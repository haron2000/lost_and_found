from django import forms
from .models import LostFoundID

class LostFoundIDForm(forms.ModelForm):
    class Meta:
        model = LostFoundID
        fields = ['id_number', 'status', 'location', 'description', 'email', 'phone_number']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially hide email and phone number fields
        self.fields['email'].required = False
        self.fields['phone_number'].required = False

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        
        # Ensure email and phone number are provided if status is 'lost'
        if status == 'lost':
            if not email:
                self.add_error('email', 'Email is required for lost IDs.')
            if not phone_number:
                self.add_error('phone_number', 'Phone number is required for lost IDs.')

class SearchIDForm(forms.Form):
    id_number = forms.CharField(label='ID Number', max_length=8)