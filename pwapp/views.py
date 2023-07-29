from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pass
from .serializers import PassSerializer
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer


class PassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer


@api_view(['GET', 'POST'])
def user(request):
    print(request.body)
    return Response({'username': 'admin'})


def pages(request):
    return Response(request)
