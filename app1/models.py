from django.db import models

# Create your models here.

class Dept(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    DName=models.CharField(max_length=50)
    Loc=models.CharField(max_length=50)
