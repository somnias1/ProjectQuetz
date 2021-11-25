from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from ..models import User
from .follows import FollowingSerializer, FollowersSerializer

from .basicinfo import (
    TutorialBasicInfoSerializer,
    UserBasicInfoSerializer,
    FollowingInfoSerializer,
)

from .tutorials import TutorialNotificacionCreacionSerializer

from .announces import ComunicadoNotificacionCreacionSerializer

from datetime import date, timedelta


class UserSerializer(serializers.ModelSerializer):
    following = FollowingInfoSerializer(many=True, read_only=True)
    tutorial_Usuario = TutorialBasicInfoSerializer(many=True, read_only=True)
    # followers = serializers.SerializerMethodField()

    class Meta:

        model = User

        fields = [
            "username",
            "last_login",
            "email",
            "fecha_registro",
            "fecha_nacimiento",
            "institucion_educativa",
            "idiomas",
            "ubicacion",
            "facebookurl",
            "twitterurl",
            "instagramurl",
            "youtubeurl",
            "adulto",
            "foto_perfil",
            "following",
            "temas_seguidos",
            "tutorial_Usuario",
        ]

    # En caso de que se necesiten todos los usuarios
    def get_users(self):
        return UserSerializer(User.objects.all(), many=True).data

    # Obtiene la información de un usuario en específico
    def get_specific_user(self, validate_data):
        infouser = User.objects.filter(username=validate_data)[0]
        return UserSerializer(infouser)

    def add_user_themes(self, user, data):
        infouser = User.objects.filter(username=user)[0]
        temas = data.pop("temas_seguidos")
        infouser.temas_seguidos.set(temas)
        return UserSerializer(infouser)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=8, max_length=86)
    password = serializers.CharField(min_length=8, max_length=64)

    # Valida la existencia de la tupla en la base de datos
    def validate(self, data):
        usuario = authenticate(username=data["username"], password=data["password"])
        if not usuario:
            raise serializers.ValidationError("Credenciales incorrectas")

        self.context["username"] = usuario
        return data

    # Si existe, permite la entrada del usuario
    # Adicionalmente, le otorga su token en caso de que no tenga uno válido
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context["username"])
        return self.context["username"], token.key


class UserSignUpSerializer(serializers.Serializer):
    # Si el usuario ya existe, retorna error
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        min_length=8,
        max_length=86,
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    fecha_nacimiento = serializers.DateField()
    # Si el email ya existe, retorna error
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Si la contraseña no coincide
    def validate(self, data):
        passwrd = data["password"]
        passwrd_conf = data["password_confirmation"]
        if passwrd != passwrd_conf:
            raise serializers.ValidationError("La contraseña no coincide")
        password_validation.validate_password(passwrd)
        return data

    def create(self, data):
        data.pop("password_confirmation")
        if (date.today() - data["fecha_nacimiento"]) > timedelta(days=18 * 365):
            user = User.objects.create_user(**data, adulto=True)
            return user

        user = User.objects.create_user(**data, adulto=False)
        return user


class UserProfileUpdateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "email",
            "institucion_educativa",
            "idiomas",
            "ubicacion",
            "facebookurl",
            "twitterurl",
            "instagramurl",
            "youtubeurl",
            "foto_perfil",
        ]

    def update_profile(self, user, data):
        infouser = User.objects.get(username=user)
        for key in data.keys():
            setattr(infouser, key, data[key])

        infouser.save()

        return UserSerializer(infouser)


class UserNotificacionSerializer(serializers.ModelSerializer):
    notificacioncreaciontutorial_set = TutorialNotificacionCreacionSerializer(
        read_only=True, many=True
    )
    notificacioncreacioncomunicado_set = ComunicadoNotificacionCreacionSerializer(
        read_only=True, many=True
    )
    followers = FollowersSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "notificacioncreaciontutorial_set",
            "followers",
            "notificacioncreacioncomunicado_set",
        )
