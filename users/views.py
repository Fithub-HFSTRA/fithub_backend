from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserGenderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)  # Return all user data, including gender

    def post(self, request, *args, **kwargs):
        user = request.user
        new_gender = request.data.get('Gender')

        # Basic validation: Ensure the gender is provided and is a valid choice
        if new_gender is None:
            return Response({"error": "Gender is required."}, status=400)
        
        valid_genders = dict(CustomUser.GENDER_CHOICES).keys()
        if new_gender not in valid_genders:
            return Response({"error": "Invalid gender provided. Please choose from 'M', 'F', or 'O'."}, status=400)

        user.gender = new_gender
        user.save(update_fields=['gender'])

        return Response({"success": "Gender updated successfully."})

class UserAge(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)  # Debug: Check the user
        if not user.is_authenticated:
            return Response({"detail": "hmmm."}, status=401)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        user = request.user
        # Extract the 'age' value from the request data
        new_age = request.data.get('Age')

        # Basic validation: Ensure the age is provided and is an integer
        if new_age is None:
            return Response({"error": "Age is required."}, status=400)

        try:
            new_age = int(new_age)  # Convert age to int and check for ValueError
            if new_age < 0 or new_age > 120:  # Basic validation for age
                raise ValueError("Invalid age.")
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        user.Age = new_age
        user.save(update_fields=['Age'])

        return Response({"success": "Age updated successfully."})

class UserWeight(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        return Response(user.Weight)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        # Extract the 'age' value from the request data
        new_weight = request.data.get('Weight')

        if new_weight is None:
            return Response({"error": "Weight is required."}, status=400)

        try:
            new_weight = int(new_weight)  
            if new_weight < 0 or new_weight > 12000:
                raise ValueError("Invalid age.")
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        user.Weight = new_weight
        user.save(update_fields=['Weight'])

        return Response({"success": "Weight updated successfully."})

class UserFriend(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        friends = user.Friends_List.all()
        friends_data = [friend.username for friend in friends]  # List of friend usernames
        print(user)
        return Response(friends_data)
        
    
    def post(self, request, *args, **kwargs):
        user = request.user
        action = request.data.get('action')
        friend_username = request.data.get('friend_username')

        if action and friend_username:
            try:
                friend = CustomUser.objects.get(username=friend_username)
                
                if action == 'add':
                    user.Friends_List.add(friend)
                    return Response({'message': 'Friend added successfully'})
                
                elif action == 'delete':
                    user.Friends_List.remove(friend)
                    return Response({'message': 'Friend removed successfully'})
                
                else:
                    return Response({'error': 'Invalid action'}, status=400)
            except user.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)
        else:
            return Response({'error': 'Missing required fields'}, status=400)
        
class HeartbeatListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        heartbeats = Heartbeat.objects.filter(user=request.user)
        serializer = HeartbeatSerializer(heartbeats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeartbeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SleepDataListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sleep_data = SleepData.objects.filter(user=request.user)
        serializer = SleepDataSerializer(sleep_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SleepDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)