from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#when yo are creating a costum user model you need to create a custom user manager

class AccountManager(BaseUserManager):
    #this function handles what happens when you create a user
     #email and password are being passed because they are the fields needed to create  a user

    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("users must have a email address")
        if not first_name:
            raise ValueError("users must have a First name")
        if not last_name:
            raise ValueError("users must have a Last name")
        
        user = self.model (
            email = self.normalize_email(email),#normalize_email just converts the email to lower case
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    #when you create a superuser
    def create_superuser(self, email, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
# Create your models here.

class Account(AbstractBaseUser):
    #unique property means that the value of that property mut be unique like a primary key.
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    username = models.CharField(default="no username",max_length=30)
    last_name = models.CharField(max_length=30)
    #these feilds are required to create a custom user model
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # you can add any oher field you wnat to add but ensure that the compostry ones are there

# this is a field that contains the feild that you want users to login with
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

#pointing the model to its user manager
    objects =  AccountManager()

    def __str__(self):
        return self.email
    #these functions are required in oder to create a custom user reg
       #this function handles permissions, who has the power to change stuff in the site
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
  

#LASTLY GO AND REFISTER YOUR CUTOM USER MODEL IN SETTINGS.PY