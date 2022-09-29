from rest_framework import serializers

from .models import Users, Stack


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    stack = StackSerializer.Meta.fields[0]

    class Meta:
        model = Users
        fields = ['id', 'name', 'surname', 'stack']
