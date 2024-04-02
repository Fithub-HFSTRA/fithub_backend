from rest_framework import serializers
from .models import CustomUser, HeartbeatSummary, SleepData

class CustomUserSerializer(serializers.ModelSerializer):
    
    friends = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'gender', 'Age', 'Weight', 'friends','first_login']  

        # The method to get the data for the 'friends' field
    def get_friends(self, obj):
        # This method returns a list of usernames of the user's friends
        return [friend.username for friend in obj.Friends_List.all()]

class HeartbeatSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartbeatSummary
        fields = ['id', 'start_time', 'end_time', 'average_bpm']

class SleepDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepData
        fields = ['id', 'start_time', 'end_time']