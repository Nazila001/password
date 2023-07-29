from rest_framework import serializers
from .models import Pass


class PassSerializer(serializers.Serializer):

    class Meta:
        model = Pass
        fields = ('id', 'author', 'name', 'url')
