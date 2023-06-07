from django.urls import path
from .views import create_test, save_iq_test_results

urlpatterns = [
    path("create-test/", create_test, name="create_test"),
    path("save-iq/", save_iq_test_results, name="save_iq_test_results"),
]
