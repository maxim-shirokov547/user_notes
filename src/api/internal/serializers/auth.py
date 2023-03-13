from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class SignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=250)
