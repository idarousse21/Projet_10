from rest_framework.serializers import ModelSerializer, CharField, EmailField
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.core.validators import MinLengthValidator


class UserSerializer(ModelSerializer):
    username = CharField(
        max_length=25,
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            MinLengthValidator(
                5, message="Le nom d'utilisateur doit contenir plus de 5 caractères."
            ),
        ],
    )
    first_name = CharField(max_length=25, required=True, label="Prénom")
    last_name = CharField(max_length=25, required=True, label="Nom")
    email = EmailField(
        max_length=255,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = CharField(
        max_length=25,
        required=True,
        label="Mot de passe",
        validators=[
            validate_password,
        ],
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
