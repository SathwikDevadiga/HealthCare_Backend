
from django.db import models
from patients.models import Patient
from doctors1.models import Doctor1 as Doctor


class Mapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.name}"

