import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, Plan,Workout_Type,Workout,Exercise
from .serializers import CustomUserSerializer, HeartbeatSummarySerializer, SleepDataSerializer, UserRegistrationSerializer
from django.utils import timezone

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "User information updated successfully."}, status=200)
        return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)  # Return all user data, including gender

class UserGenderView(APIView):
    permission_classes = [IsAuthenticated]

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

        return Response({"success": "Gender updated successfully."}, status=200)
    
def stringIntoDateTime(string):
    print("whaaa",string)
    return "what"

class startExercise(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        #check to see if latest exercise is still going
        if(user.exercises.all().count() > 0):
            latestExercise = user.exercises.all().last()
            if(latestExercise.end_time == None):
                return Response({"error": "User is already exercising"}, status=400)
        user.is_working = True
        ins_wt, _ =  Workout_Type.objects.get_or_create(name=request.data.get('name'))
        exercise = Exercise.objects.create(
            workout_type=ins_wt,
            start_time = timezone.now(),
            end_time = None,
            fuffilment = False,
        )
        user.exercises.add(exercise)

class endExercise(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        #check to see if latest exercise is still going
        if(user.exercises.all().count() == 0 or user.exercises.all().last().end_time != None):
            return Response({"error": "User is not exercising"}, status=400)
        #check to see if it hasn't been too long since the excercise started
        user.is_working = False
        exercise = user.exercises.all().last()
        exercise.end_time = stringIntoDateTime(request.data.get('end_time'))

class getAllExercises(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        print('dink')
        #check to see if latest exercise is still going
        iter_list = user.exercises.all()
        ret_list = []
        for itera in iter_list:
            ret_list.append({
                "start":str(itera.start_time),
                "end":str(itera.end_time),
                "name":itera.workout_type.name,
                "category":itera.workout_type.category
            })
        data = {
            'ex': ret_list,
        }
        
        return Response(data)

class UserAge(APIView):
    permission_classes = [IsAuthenticated]

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

        user.age = new_age
        user.save(update_fields=['Age'])

        return Response({"success": "Age updated successfully."}, status=200)


class UserWeight(APIView):
    permission_classes = [IsAuthenticated]

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

        return Response({"success": "Weight updated successfully."}, status=200)

class UserPlan(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        # Get the plan data from the request
        name = request.data.get('plan_name')
        description = request.data.get('description')
        difficulty_level = request.data.get('difficulty_level')
        workouts_data = request.data.get('workout_days')

        # Create a new plan instance
        plan = Plan.objects.create(
            name=name,
            creator=user,
            description=description,
            difficulty_level=difficulty_level
        )

        # Create workout instances and associate them with the plan
        for workout_data in workouts_data:
            workout_type_name = workout_data.get('name')
            workout_days = workout_data.get('days')
            workout_length = workout_data.get('time')
            description = workout_data.get('description')
            equipment_needed = workout_data.get('equipment_needed')
            
            workout_type, _ = Workout_Type.objects.get_or_create(name=workout_type_name.strip(), defaults={'name': workout_type_name})
            workout = Workout.objects.create(
                workout_type=workout_type,
                workout_days=workout_days,
                workout_length=workout_length,
                description=description,
                equipment_needed=equipment_needed
            )
            plan.workouts.add(workout)

        # Assign the created plan to the user
        user.current_workout_plan = plan
        user.save()

        return Response({'message': 'Custom plan created and assigned successfully.'})

    def get(self, request, *args, **kwargs):
        user = request.user
        plan = user.current_workout_plan
        if(plan == None or plan.workouts.all().count() == 0):
            print("what? thre's no plans?")
            return Response(None);
        workouts = plan.workouts.all()
        
        # Create a list to store exercises for each day of the week
        workout_days = [[] for _ in range(7)]
        
        for workout in workouts:
            # Convert the workout_days integer to a binary string
            # Iterate over each day of the week
            for day in range(7):
                if workout.workout_days & (1 << day):
                    # If the day is active, add the workout to the corresponding day's list
                    workout_days[day].append({
                        "name": str(workout),
                        "type": str(workout.workout_type.category),
                        "time": workout.workout_length
                    })
        
        data = {
            'workout_days': workout_days,
            "plan_name": plan.name
        }
        
        return Response(data)
class UserWorkoutTypes(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        Workout_Types = Workout_Type.objects.all()
        if(Workout_Types == None or Workout_Types.count() == 0):
            return Response("ERROR: No workout types found");        
        # Create a list to store exercises for each day of the week
        Workout_Types_Results = []
        
        for workout_type in Workout_Types:
            Workout_Types_Results.append({
                "name": str(workout_type.name),
                "category": str(workout_type.category),
            })
        
        data = {
            'workout_types': Workout_Types_Results,
        }
        
        return Response(data)

    

class UserFriend(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        #friends = user.Friends_List.all()
        #if not friends.exists():  # Check if the user has no friends
        #    return Response(None)  # Return `null` if there are no friends
        #friends_data = [friend.username for friend in friends]
        #return Response(friends_data)
        friends = [friend.username for friend in user.Friends_List.all()]
        sent_friend_requests = [user.username for user in user.pending_friend_requests.all()]
        received_friend_requests = [user.username for user in user.received_friend_requests.all()]

        data = {
            'friends': friends,
            'sent_friend_requests': sent_friend_requests,
            'received_friend_requests': received_friend_requests
        }

        return Response(data)
        
    
    def post(self, request, *args, **kwargs):
        user = request.user
        action = request.data.get('action')
        friend_username = request.data.get('friend_username')

        if action and friend_username:
            try:
                friend = CustomUser.objects.get(username=friend_username)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=404)

            if action == 'send_request':
                # Logic to send a friend request
                user.pending_friend_requests.add(friend)
                return Response({'message': 'Friend request sent successfully'}, status=200)

            elif action == 'accept_request':
                # Logic to accept a friend request
                if friend in user.received_friend_requests.all():
                    user.Friends_List.add(friend)
                    user.received_friend_requests.remove(friend)
                    friend.Friends_List.add(user)  # Ensure friendship is mutual
                    return Response({'message': 'Friend request accepted'}, status=200)
                else:
                    return Response({'error': 'Friend request not found'}, status=404)

            elif action == 'delete_friend':
                # Logic to delete a confirmed friend
                if friend in user.Friends_List.all():
                    #user.friends.remove(friend)
                    user.Friends_List.remove(friend)
                    #friend.friends.remove(user)  # Ensure to remove from both sides
                    friend.Friends_List.remove(user) 
                    return Response({'message': 'Friend removed successfully'}, status=200)
                else:
                    return Response({'error': 'Friend not found in friend list'}, status=404)

            elif action == 'cancel_request':
                # Logic to cancel a sent friend request
                if friend in user.pending_friend_requests.all():
                    user.pending_friend_requests.remove(friend)
                    return Response({'message': 'Friend request cancelled'}, status=200)
                else:
                    return Response({'error': 'Friend request not found'}, status=404)

            elif action == 'reject_request':
                # Logic to reject a received friend request
                if friend in user.received_friend_requests.all():
                    user.received_friend_requests.remove(friend)
                    return Response({'message': 'Friend request rejected'}, status=200)
                else:
                    return Response({'error': 'Friend request not found'}, status=404)

            else:
                return Response({'error': 'Invalid action'}, status=400)
        return Response({'error': 'must specify friend+action'}, status=400)
        
class HeartbeatSummary(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Correctly access the related HeartbeatSummary objects using the related_name
        summaries = request.user.heartbeat_summaries.all()  # Use the related_name 'heartbeat_summaries'
        if summaries.exists():
            serializer = HeartbeatSummarySerializer(summaries, many=True)
            return Response(serializer.data)
        else:
            return Response('null')  # Return `null` if there are no summaries

    def post(self, request):
        serializer = HeartbeatSummarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response('success', status=201)
        return Response('error', status=400)
    
class SleepData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Correctly access the related HeartbeatSummary objects using the related_name
        summaries = request.user.sleepdata.all()  # Use the related_name 'heartbeat_summaries'
        if summaries.exists():
            serializer = SleepDataSerializer(summaries, many=True)
            return Response(serializer.data)
        else:
            return Response('null')  # Return `null` if there are no summaries

    def post(self, request):
        serializer = SleepDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response('success', status=201)
        return Response('error', status=400)

class NameData(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        new_first_name = request.data.get('first_name')
        new_last_name = request.data.get('last_name')

        #validation
        if (new_first_name or new_last_name) is None:
            return Response({"error": "First name and last name is required."}, status=400)
        
        #store
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.save(update_fields=['first_name'])
        user.save(update_fields=['last_name'])
        return Response({"success": "Name updated successfully."}, status=200)
    
#For user register API
class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=201)
        return Response(serializer.errors, status=400)