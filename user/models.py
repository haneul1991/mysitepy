from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return 'User(%s, %s, %s)' %(self.email, self.name, self.gender)