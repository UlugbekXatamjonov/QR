# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import MinLengthValidator

# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.utils import timezone


# class UserManager(BaseUserManager):

#     def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()
#         if not username:
#             raise ValueError(('The given username must be set'))
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email,
#                           is_staff=is_staff, is_active=True,
#                           is_superuser=is_superuser, last_login=now,
#                           **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         return self._create_user(username, email, password, False, False, ' ',
#                                  **extra_fields)

#     def create_superuser(self, username, email, password, **extra_fields):
#         user = self._create_user(username, email, password, True, True,
#                                  **extra_fields)
#         user.is_active = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=30, unique=True)
#     name = models.CharField(max_length=70)
#     email = models.EmailField(max_length=250, unique=True)
#     birth_date = models.DateField(auto_now=False, auto_now_add=False,  null=True)
#     profile_image = models.ImageField(upload_to='Profile_Pic/%Y/%m/%d/', null=True, blank=True, verbose_name='Foydalanuvchi rasmi',)
#     position = models.CharField(max_length=150, null=True)
    
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now=True, null=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', ]




# class User(models.Model):
# 	username = models.CharField(max_length=100, unique=True, verbose_name='Username')
# 	first_name = models.CharField(max_length=100, verbose_name='Ism')
# 	last_name = models.CharField(max_length=100, verbose_name='Familya')
# 	password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])
# 	email = models.EmailField(verbose_name='Email', unique=True)
# 	position = models.CharField(max_length=150)
# 	data_of_birth = models.DateField(auto_now=False, auto_now_add=False)
# 	photo = models.ImageField(upload_to='Profile_Pic/%Y/%m/%d/', verbose_name='Foydalanuvchi rasmi', null=True, blank=True)
	
# 	# USERNAME_FIELD = 'username'
# 	# REQUIRED_FIELDS = ["email", "password"]

# 	def __str__(self):
# 		return self.username





