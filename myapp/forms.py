from django import forms
from django.contrib.auth import get_user_model
from .models import Message
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "icon")

class LoginForm(AuthenticationForm):
    pass

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("message",)
        
class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username",)
        labels = {"username": "新しいユーザーネーム"}

class ChangeMailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {"email": "新しいメールアドレス"}
        
class ChangeIconForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("icon",)
        
class ChangePasswordForm(PasswordChangeForm):
    """パスワードを変更するフォーム"""