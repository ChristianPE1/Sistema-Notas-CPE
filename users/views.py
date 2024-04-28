from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import RegisterUserSerializer, MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
   data = request.data
   if User.objects.filter(email=data['email']).exists():
      return Response({'error': 'Email already exists'})
   user = User.objects.create(
      email=data['email'],
      name=data['name'],
      last_name=data['last_name'],
      password=make_password(data['password']),
      is_teacher=data['is_teacher']
   )
   serializer = RegisterUserSerializer(user, many=False)
   return Response(serializer.data)

class LoginView(TokenObtainPairView):
   serializer_class = MyTokenObtainPairSerializer