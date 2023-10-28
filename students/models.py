from django.db import models

# Create your models here.
class Student(models.Model):
  index_number = models.PositiveIntegerField()
  reg_number = models.CharField(max_length=10)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=150)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'