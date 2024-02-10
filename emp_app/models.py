from django.db import models

class add_emp(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)
    phone=models.IntegerField()
    description=models.CharField(max_length=200)
