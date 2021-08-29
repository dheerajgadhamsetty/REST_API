from django.db import models

# Create your models here.
class Manager(models.Model):
    Firstname = models.CharField(max_length=10)
    Lastname = models.CharField(max_length=10)
    m_id = models.IntegerField()
    m_phone_no = models.IntegerField()
    m_salary = models.IntegerField()

    def __str__(self):
        return '%s' %self.Firstname


