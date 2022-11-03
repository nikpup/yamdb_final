from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import YaUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = YaUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = YaUser
        fields = ('username', 'email', 'first_name', 'last_name')
