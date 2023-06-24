from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['GET'])
    def teachers(self, request):
        teachers = self.get_queryset().filter(role='teacher')
        serializer = self.get_serializer(teachers, many=True)
        # teacher_names = teachers.values_list('name', flat=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def check_password(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'Both username and password are required.'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        is_password_correct = user.check_password(password)

        if is_password_correct:
            return Response({'detail': 'Password is correct.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
