from rest_framework.serializers import ModelSerializer, CharField,EmailField
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class UserSerializer(ModelSerializer):
    username = CharField(max_length=25,required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = CharField(max_length=25, required=True)
    last_name = CharField(max_length=25, required=True)
    email = EmailField(max_length=255,required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(
        validators=[validate_password]
    )
    class Meta:
        model = User
        fields = ("id","username","first_name", "last_name", "email", "password", )
