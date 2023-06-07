from rest_framework import serializers
from .models import IQEQTest


class IQEQSerializer(serializers.ModelSerializer):
    class Meta:
        model = IQEQTest
        fields = ["login"]
