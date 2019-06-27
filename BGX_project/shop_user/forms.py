from django import forms
from django.contrib.auth import get_user_model
from shop_user.models import UserGoodsComment

MyUser = get_user_model()


class UserLoginFrom(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)#,widget=forms.PasswordInput(attrs={'class':'username'}))
    password = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())

class SearchForm(forms.Form):
    content = forms.CharField(max_length=20)




# class RegFrom(forms.Form):
#     name = forms.CharField(max_length=20, min_length=2)
#     password = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())

class RegForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("username", "password")
        widgets = {
            "password": forms.PasswordInput()
        }
        help_texts = {
            "username": ''
        }

class UserGoodsCommentForm(forms.ModelForm):

    class Meta:
        model = UserGoodsComment
        fields = ("user", "goods", "context")

    # def save(self, commit=True):

# class RegFrom(forms.Form):
#     name = forms.CharField(max_length=20,min_length=4)
#     pwd = forms.CharField(max_length=255,min_length=6,widget=forms.PasswordInput())