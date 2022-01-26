from django import forms
from posts.models import Image


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput()
    )
    age = forms.IntegerField(min_value=18, required=False)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')
