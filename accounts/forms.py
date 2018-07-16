from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.files import File
from django.forms.widgets import FileInput
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User.objects.get(email__iexact=email)
            raise forms.ValidationError('email already exists')
        except User.DoesNotExist:
            return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'country')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs={
            'class':'form-control border-input',
            }

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs={
            'class':'form-control border-input',
            }

        self.fields['first_name'].required = True
        self.fields['first_name'].widget.attrs={
            'class':'form-control border-input',
            }

        self.fields['last_name'].required = True
        self.fields['last_name'].widget.attrs={
            'class':'form-control border-input',
            }

        self.fields['country'].required = True
        self.fields['country'].widget.attrs={
            'class':'form-control',
            }

class FileUploadForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('upload',)

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['upload'].label = ''
        self.fields['upload'].name= ''
        
class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password',)
        
