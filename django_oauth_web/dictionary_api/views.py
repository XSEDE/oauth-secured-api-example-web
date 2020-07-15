from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

# Create your views here.
class Dictionary_API(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        return Response({}, template_name='index.html')

