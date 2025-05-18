from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True) 
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('super user must have is_staff true')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user must have is_superuser true')

        
        return self.create_user(email,password,**extra_fields)
class CustomUser(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    objects=CustomUserManager()
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?\d{9,15}$')],
        unique=True,
        null=True,
        blank=True,
        help_text="Enter phone number in format: +251912345678"
    )

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['full_name']

    def __str__(self):
        return self.email


