from django.db import models


# Create your models here.
class Employee(models.Model):
    # id=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    phone_no=models.PositiveIntegerField()
    department=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()