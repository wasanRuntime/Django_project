from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format = None):
        """Returns list of APIView features."""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete'
            'It is similar to a traditional Django view'
            'Gives you the most control over your view'
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview}, status=status.HTTP_200_OK)