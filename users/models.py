from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
import uuid

class CustomUserManager(UserManager):
   def _create_user(self, email, password, **extra_fields):
      if not email:
         raise ValueError('Debes tener un email')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_user(self, email=None,password=None,**extra_fields):
      extra_fields.setdefault('is_admin',False)
      return self._create_user(email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
   id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
   email = models.EmailField(unique=True)
   name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   avatar = models.URLField(max_length=200)
   date_joined = models.DateTimeField(default=timezone.now)
   is_admin = models.BooleanField(default=False)
   objects = CustomUserManager()
   is_teacher = models.BooleanField(default=False)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

   class Meta:
      ordering = ['date_joined']