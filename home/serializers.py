# serializers.py
from rest_framework import serializers

from .models import UserData

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ('id','email','name')