from rest_framework import serializers
from app.models import User

from app.models import Articles

class UserSerializer(serializers.ModelSerializer):
    """UserSerializer Class"""

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

    
    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return: user
        """
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            bio=validated_data['bio']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ArticlesSerializer(serializers.ModelSerializer):
    """ArticlesSerializer Class"""

    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Articles
        fields = (
            'id', 'title',
            'content', 'upload',
            'author', 'created',
            'modified',
        )

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)