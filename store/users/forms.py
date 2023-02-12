from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User

