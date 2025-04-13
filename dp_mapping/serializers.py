from rest_framework import serializers
from .models import Mapping
from patients.models import Patient
from doctors1.models import Doctor1 as Doctor

class MappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Mapping
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name']
