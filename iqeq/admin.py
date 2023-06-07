from django.contrib import admin
from .models import IQEQTest, IQTestResults, EQTestResults

admin.site.register(IQEQTest)
admin.site.register(IQTestResults)
admin.site.register(EQTestResults)
