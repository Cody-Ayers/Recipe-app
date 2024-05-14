from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=75)

    def __str__(self):
        return str(self.name)
    
    