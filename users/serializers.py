from rest_framework import serializers
from .models import CustomUser, HeartbeatSummary, SleepData
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    
    friends = serializers.SerializerMethodField()
    sent_friend_requests = serializers.SerializerMethodField()
    received_friend_requests = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'age', 'weight', 'friends','first_login','sent_friend_requests', 'received_friend_requests']  

        # The method to get the data for the 'friends' field
    def get_friends(self, obj):
        # This method returns a list of usernames of the user's friends
        return [friend.username for friend in obj.friends_list.all()]
    
    def get_sent_friend_requests(self, obj):
        return [user.username for user in obj.pending_friend_requests.all()]

    def get_received_friend_requests(self, obj):
        return [user.username for user in obj.received_friend_requests.all()]

class HeartbeatSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartbeatSummary
        fields = ['id', 'start_time', 'end_time', 'average_bpm']

class SleepDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepData
        fields = ['id', 'start_time', 'end_time']

#For user register api
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)