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


class EQTestResultsSerializer(serializers.ModelSerializer):
    allowed_letters = {"а", "б", "в", "г", "д"}

    def validate_letters(self, value):
        for char in value:
            if char.lower() not in self.allowed_letters:
                raise serializers.ValidationError(f"Недопустимый символ: {char}")

        if len(value) != 5:
            raise serializers.ValidationError(
                "Результаты теста должны содержать 5 ответов"
            )
        return value

    class Meta:
        model = EQTestResults
        fields = ["login", "letters"]
