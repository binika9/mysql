from django.db import models
from django import forms



# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    mobile_no = models.CharField(max_length=10)
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname


class registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name

class next_of_kin(models.Model):
    fullname = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    id_no = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)


