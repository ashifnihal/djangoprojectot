from django import forms
from blog import models
class EmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    class Meta:
        model=models.CommentModel
        fields=('name','email','body')
