from django.db.models import fields
from rest_framework import serializers
from apps.usuarios.models import User 

# Serializador basado en un modelo
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'