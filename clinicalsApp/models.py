from django.db import models


# Create your models here.
class Patient(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()


class ClinicalData(models.Model):
    componentName = models.CharField(max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
