from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['email', 'name', 'last_name', 'password','is_teacher']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   @classmethod
   def get_token(cls, user):
      token = super().get_token(user)
      token['email'] = user.email
      token['is_admin'] = user.is_admin
      return token