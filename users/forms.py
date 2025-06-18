from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

