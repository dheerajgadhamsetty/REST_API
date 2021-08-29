from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=10)
    secondname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

def __str__(self):
    return '%s' %self.firstname
    


