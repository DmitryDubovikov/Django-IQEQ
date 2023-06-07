from django.db import models


class IQEQTest(models.Model):
    login = models.CharField(max_length=10, unique=True)


class IQTestResults(models.Model):
    login = models.ForeignKey(IQEQTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    time_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IQ test results of {self.login}"


class EQTestResults(models.Model):
    login = models.ForeignKey(IQEQTest, on_delete=models.CASCADE)
    letters = models.CharField(max_length=5)
    time_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EQ test results of {self.login}"
