from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ArchivoPDF
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = ('username','idTipo','numdoc','first_name','last_name','email','telefono','password1','password2')

class ActualizacionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','telefono','is_active']

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = ArchivoPDF
        fields = ('title', 'file',)