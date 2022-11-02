from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class List(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=200 ,default="")
    Complete=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default='1', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email, user_name, first_name, password , **extra_fields):

        email=self.normalize_email(email)
        user= self.model(email=email,user_name=user_name, **extra_fields )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self , email, user_name, first_name, password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff true')

        return self.create_user(email, user_name, first_name, password , **extra_fields)        


class User(AbstractUser, PermissionsMixin):
    user_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True , max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    objects=UserManager()

    def __str__(self):
        return self.user_name