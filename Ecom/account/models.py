from django.db import models

# Create your models here.
class Registration(models.Model):
    fullname = models.CharField(max_length=150)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username