from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions, status


@api_view(['GET'])
def get_current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        email = request.data.get('email', None)
        password1 = request.data.get('password1', None)
        password2 = request.data.get('password2', None)
        firstName = request.data.get('firstName', None)
        lastName = request.data.get('lastName', None)
        if not email or not password1 or password1 != password2:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializerWithToken(data={
            'full_name': '{} {}'.format(firstName, lastName),
            'email': email,
            'password': password1
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
