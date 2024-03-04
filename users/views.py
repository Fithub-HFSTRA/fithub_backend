from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserGenderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)  # Debug: Check the user
        if not user.is_authenticated:
            return Response({"detail": "hmmm."}, status=401)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
