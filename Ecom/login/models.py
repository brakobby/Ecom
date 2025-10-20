from django.db import models
 
# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
