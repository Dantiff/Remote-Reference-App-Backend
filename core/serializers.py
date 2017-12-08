
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User, Group
from core.models import *

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
               validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
            required=True,
            max_length=32
            )

    def create(self, validated_data):
        profile = Profile.objects.create_user_profile(validated_data['phone'], validated_data['national_id'])
        return profile

    class Meta:
        model = Profile
        fields = ('id', 'phone')


class DueListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueListing
        fields = ('id', 'customer', 'debtor', 'debt_status', 'amount')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')