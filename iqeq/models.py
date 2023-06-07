from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class IQEQTest(models.Model):
    login = models.CharField(max_length=10, unique=True, primary_key=True)

    def __str__(self):
        return f"IQEQ test of {self.login}"


class IQTestResults(models.Model):
    login = models.ForeignKey(IQEQTest, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    time_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IQ test results of {self.login}"


class EQTestResults(models.Model):
    login = models.ForeignKey(IQEQTest, on_delete=models.CASCADE)
    letters = models.CharField(max_length=5)
    time_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EQ test results of {self.login}"
