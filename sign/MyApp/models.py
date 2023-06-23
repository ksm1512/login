from django.db import models

# Create your models here.
class Student(models.Model):
    uname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pass1 = models.CharField(max_length=30)
    pass2 = models.CharField(max_length=30)