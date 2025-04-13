from rest_framework import serializers
from .models import Doctor1

class DocatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor1
        fields = '__all__'
        read_only_fields = ['user']
