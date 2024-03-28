from django.db import models

# Create your models here.
class PersonalData(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    def __str__(self):
        return self.firstname
    

    
