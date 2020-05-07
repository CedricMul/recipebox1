from django import forms
from recipebox.models import Author
from django.contrib.auth.models import User

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())

    def __str__(self):
        return self.name
    
    def url(self):
        return self.name.replace(" ", "_").lower()

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required=forms.CharField(max_length=20)
    instructions=forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.title
    
    def url(self):
        return self.title.replace(" ", "_").lower()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
