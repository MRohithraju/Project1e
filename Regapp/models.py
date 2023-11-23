from django.db import models

# Create your models here.
class Reg(models.Model):
    fristname=models.CharField(max_length=14)
    lastname=models.CharField(max_length=15)
    username=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=15)
    cpassword=models.CharField(max_length=15)
    emailid=models.EmailField()
    mobileno=models.IntegerField()

