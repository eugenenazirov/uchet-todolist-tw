from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.request import Request


class EmailOrPhoneBackend(ModelBackend):
    """
        Custom Auth Backend to perform authentication via email or phone
        Uses 'email' or 'phone' field in request to log in.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(email=email) |
                Q(phone_number=request.data.get('phone_number'))
            )
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        except TypeError:
            return None
        except AttributeError:
            return None

    def get_user(self, user_id):
        my_user_model = get_user_model()
        try:
            return my_user_model.objects.get(pk=user_id)
        except my_user_model.DoesNotExist:
            return None
