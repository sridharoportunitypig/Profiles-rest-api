from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class HelloSerializer(serializers.Serializer):
    """serializers a user profiles objects"""


class UserProfileSerializer(serializers.ModelSerializer):
    """serializers a user profiles object"""

    class Meta:
        model = models.UserProfile
        fields =('id', 'email', 'name', 'password')
        extra_kwarg = {
            'password':{
                 'write_only':True,
                 'style':{'input_type':'password'}
            }
        }


    def create(self,validated_data):
        """Create and return new user"""

        user = models.UserProfile.objects.create_user(
        email = validated_data['email'],
        name = validated_data['name'],
        password = validated_data['password'],

        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwarg = {'user_profile':{'read_only':True}}
