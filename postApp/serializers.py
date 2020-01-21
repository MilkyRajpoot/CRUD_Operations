from .models import postApi
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = postApi
        fields = ('name', 'profile', 'place')