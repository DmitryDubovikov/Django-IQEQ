from rest_framework import serializers
from .models import IQEQTest, IQTestResults, EQTestResults


class IQEQSerializer(serializers.ModelSerializer):
    class Meta:
        model = IQEQTest
        fields = ["login"]


class IQTestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IQTestResults
        fields = ["login", "score"]
