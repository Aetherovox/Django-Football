from django.contrib.auth.models import User
from rest_framework.serializers import (ModelSerializer, CharField,EmailField)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import TokenizedUser

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(TokenObtainPairSerializer,cls).get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        return token

class CustomUserSerializer(ModelSerializer):
    email = EmailField(required=True)
    username = CharField()
    password = CharField(min_length=8,max_length=32,write_only=True)

    class Meta:
        model = TokenizedUser
        # fields = ('email','username','password')
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

