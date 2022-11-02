from django.db import models

# Create your models here.
class task(models.Model):
    heading=models.CharField(max_length=70)
    detail=models.CharField(max_length=70)
    date=models.DateField()
    is_deleted=models.CharField(max_length=2)
