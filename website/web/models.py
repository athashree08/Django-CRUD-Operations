from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


    class Meta:
        db_table = 'student'

# Create your models here.
