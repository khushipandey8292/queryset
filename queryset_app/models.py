from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=60)
    marks=models.IntegerField()
    pass_date=models.DateField()


class Teacher(models.Model):
    name=models.CharField(max_length=60)
    teachnumber=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=50)
    salary=models.IntegerField()
    join_date=models.DateField()