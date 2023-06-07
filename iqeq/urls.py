from django.urls import path
from .views import create_test

urlpatterns = [
    path("create-test/", create_test, name="create_test"),
]
