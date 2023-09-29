from rest_framework.serializers import ModelSerializer, Serializer

from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.serializers import UserSerializer
from guests.models import Guest

User = get_user_model()

class GuestSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Guest
        fields = ['id', 'user', 'birthdate', 'age', 'gender']
        extra_kwargs = {
            'id': {'read_only': True, 'required': False}
        }
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print("create", user_data)
        user = Guest.objects.create_user(user_type=User.GUEST, **user_data)
        guest = Guest.objects.create(user=user, **validated_data)
        return guest