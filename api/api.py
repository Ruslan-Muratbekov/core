from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import UpdateAPIView
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, EventSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django_filters import rest_framework
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticated

from user.models import User
from event.models import Event


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        password = request.data['password']
        print(email, password)

        user = User.objects.filter(email=email)

        if user:
            return Response({'message': 'Пользователь уже есть'}, status.HTTP_403_FORBIDDEN)
        else:
            create_user = User.objects.create_user(email, password)

            if create_user:
                user_as_dict = UserSerializer(create_user, many=False)

                return Response(user_as_dict.data, status.HTTP_201_CREATED)

            return Response({'message': 'Ошибка'}, status.HTTP_401_UNAUTHORIZED)


class LoginGenericAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)

        if user:
            user_as_dict = UserSerializer(data=user, many=False)

            return Response(user_as_dict.data, status.HTTP_200_OK)
        else:
            return Response({'message': 'Ошибка'}, status.HTTP_401_UNAUTHORIZED)


class EventModelViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user',)


class EventUpdateModelViewSet(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id',)
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pk'
