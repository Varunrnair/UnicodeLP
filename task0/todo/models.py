from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class List(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField(max_length=200 ,default="")
    Complete=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email, first_name, password , **extra_fields):

        email=self.normalize_email(email)
        user= self.model(email=email, **extra_fields )
        extra_fields.setdefault('is_active', True)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self , email, first_name, password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff true')

        return self.create_user(email, first_name, password , **extra_fields)        


class User(AbstractUser, PermissionsMixin):
    #user_name=models.CharField(unique = True, max_length=50)
    email=models.EmailField(unique = True, max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    profile_pic=models.ImageField(null=True, blank=True, upload_to='todo/images')
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects=UserManager()

    def __str__(self):
        return self.email