from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.username}"
    
class fUser(models.Model):
    fusername = models.CharField(max_length=255, null=True)
    fpassword = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.fusername}"
