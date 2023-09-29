from rest_framework.serializers import ModelSerializer, Serializer

from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.serializers import UserSerializer
from maids.models import Maid

User = get_user_model()

class MaidSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Maid
        fields = ['id', 'user', 'birthdate', 'age', 'gender']
        extra_kwargs = {
            'id': {'read_only': True, 'required': False}
        }
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print("create", user_data)
        user = User.objects.create_user(user_type=User.MAID, **user_data)
        maid = Maid.objects.create(user=user, **validated_data)
        return maid