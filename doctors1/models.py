
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



class Doctor1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,blank=False)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(blank=False, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name