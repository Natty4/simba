from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validator import PhoneValidator



class User(AbstractUser):
	username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
	email = models.EmailField(_('email address'), unique = True)
	
	phone_number = models.CharField(_('phone number'), max_length = 10, validators=[PhoneValidator()], unique = True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name', 'username']
	
	def __str__(self):
		return "{}".format(self.email)


