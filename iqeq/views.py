from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import string
import random
from .models import IQEQTest
from .serializers import IQEQSerializer

# Create your views here.


@api_view(["POST"])
def create_test(request):
    login = "".join(random.choices(string.ascii_letters, k=10))
    test = IQEQTest.objects.create(login=login)
    serializer = IQEQSerializer(test)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
