from django import forms
from accounts.models import Member

class RegisterMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['member_name', 'member_email', 'member_contact']
        widgets = {
            'member_name':forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'member_email':forms.EmailInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'member_contact':forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
        }