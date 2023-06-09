from django.http import HttpResponseBadRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import string
import random
from .models import IQEQTest, IQTestResults, EQTestResults
from .serializers import (
    IQEQTestSerializer,
    IQTestResultsSerializer,
    EQTestResultsSerializer,
)


@api_view(["POST"])
def create_test(request):
    login = "".join(random.choices(string.ascii_letters, k=10))
    test = IQEQTest.objects.create(login=login)
    serializer = IQEQTestSerializer(test)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def save_iq_test_results(request):
    test_serializer = IQTestResultsSerializer(data=request.data)
    test_serializer.is_valid(raise_exception=True)
    test_serializer.save()
    return Response(test_serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def save_eq_test_results(request):
    test_serializer = EQTestResultsSerializer(data=request.data)
    test_serializer.is_valid(raise_exception=True)
    test_serializer.save()
    return Response(test_serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def results(request):
    login = request.data.get("login")
    if not login:
        return HttpResponseBadRequest("Отсутствует обязательный параметр 'login'")

    eq_results = EQTestResults.objects.filter(login=login)
    eq_serializer = EQTestResultsSerializer(eq_results, many=True)

    iq_results = IQTestResults.objects.filter(login=login)
    iq_serializer = IQTestResultsSerializer(iq_results, many=True)
    return Response(
        {"IQ results": iq_serializer.data, "EQ results": eq_serializer.data}
    )
