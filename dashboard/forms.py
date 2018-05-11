from django import forms
from django.contrib.auth.models import User

from .models import Post, Collection

class HomePageLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(min_length=7, widget=forms.PasswordInput)

    class Meta:
        fields = ["username", "password"]

    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     if username == 'admin':
    #         raise forms.ValidationError("Invalid! That's a reserved username.")
    #     return username


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "summary"]


class SaveToCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["title", "posts"]
