from django import forms
from Posts.models import Post


class PostAddModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Text']
