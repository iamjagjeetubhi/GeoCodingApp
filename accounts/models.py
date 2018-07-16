from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from accounts.validation import validate_file_extension

class User(AbstractUser):
    country = CountryField(blank=True)
    upload = models.FileField(upload_to='uploaded_files/', validators=[validate_file_extension])

		
