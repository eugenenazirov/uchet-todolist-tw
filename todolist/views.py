from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .settings import DJOSER as djoser_settings
from djoser.views import UserViewSet


class PasswordResetConfirmationView(UserViewSet):
    """
    This view handles GET requests and renders a template for password reset.
    This template contains form for new password entering
    and sending POST request to the same url to change the password
    You can just use 'uid' and 'token' from it to create your own POST request
    """
    permission_classes = []

    def get_reset_template(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + '/' + djoser_settings.get('PASSWORD_RESET_CONFIRM_URL')
        context = {
            'token': token,
            'uid': uid,
            'form_url': request.get_full_path()
        }

        return render(request, template_name='password_reset_confirm.html', context=context)
