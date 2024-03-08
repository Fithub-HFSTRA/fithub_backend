from rest_framework import serializers
from .models import CustomUser, Heartbeat, SleepData

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'gender', 'Age', 'Weight', 'friends']  

        # The method to get the data for the 'friends' field
    def get_friends(self, obj):
        # This method returns a list of usernames of the user's friends
        return [friend.username for friend in obj.Friends_List.all()]

class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ['id', 'timestamp', 'beats_per_minute']

class SleepDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepData
        fields = ['id', 'start_time', 'end_time']