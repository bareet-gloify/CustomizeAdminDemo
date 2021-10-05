from django.db import models

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=50)
    college_address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    college = models.ForeignKey(
        College, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    std = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    student_address = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
