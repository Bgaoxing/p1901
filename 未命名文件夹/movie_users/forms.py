from django import forms
from django.contrib.auth import get_user_model
from movie_users.models import UserMovieComment

MyUser = get_user_model()


class UserLoginFrom(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)
    password = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())

# class RegFrom(forms.Form):
#     name = forms.CharField(max_length=20, min_length=2)
#     password = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())

class RegForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("username", "password")
        widgets = {
            "password":forms.PasswordInput()
        }

class UserMovieCommentForm(forms.ModelForm):

    class Meta:
        model = UserMovieComment
        fields = ("user", "movie", "context")

    # def save(self, commit=True):

# class RegFrom(forms.Form):
#     name = forms.CharField(max_length=20,min_length=4)
#     pwd = forms.CharField(max_length=255,min_length=6,widget=forms.PasswordInput())