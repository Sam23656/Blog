from django import forms

from Posts.models import Post


class PostAddModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Text']


class UserPasswordResetForm(forms.Form):
    Name = forms.CharField()
    New_Password = forms.CharField()
    Confirm_Password = forms.CharField()
