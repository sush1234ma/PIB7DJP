from django.db import models

# Create your models here.

class students(models.Model) :                                                       # 7
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    jdate = models.DateField()

    def __str__(self):                                                                   # 7.1
        return self.student_name                                   # the row displayed by this name

