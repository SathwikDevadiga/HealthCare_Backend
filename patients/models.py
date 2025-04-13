from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=False)
    age = models.IntegerField( validators=[MinValueValidator(0),MaxValueValidator(120)], blank=False)
    gender = models.CharField(validators=[MinValueValidator(1)])
    medical_history = models.TextField()

    def __str__(self):
        return self.name
