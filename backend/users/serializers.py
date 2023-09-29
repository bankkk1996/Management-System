from rest_framework.serializers import ModelSerializer, Serializer

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'user_type',
                  'groups'
                  )
        extra_kwargs = {
            'id': {'read_only': True, 'required': False},
            'user_type': {'read_only': True, 'required': False},
            'username': {'required': False, 'validators': []},
            'password': {'write_only': True, 'required': False},
            'groups': {'read_only': True, 'required': False},
        }
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()
        return user