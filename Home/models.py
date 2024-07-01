import re

from django.core.exceptions import ValidationError

from django.db import models


class details(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    
class Meta:
        verbose_name_plural = "All Details"

def clean(self):
        super().clean()
        email = self.Email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("Enter a valid email address")
