from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_number = models.CharField(max_length=50)

    def __str__(self):
        return self.student_number