from django import forms
import projectapp
from projectapp.models import Facescan
class ImageForm(forms.ModelForm):
    class Meta:
        model=Facescan
        fields=('username','image')