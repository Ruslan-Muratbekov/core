from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer, EventSerializer, ThemeSerializer, \
    EventCreateSerializer, EventSubscribeSerializer, EventReadonlySubscribeSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCheck
from django.shortcuts import get_object_or_404

from user.models import User
from event.models import Event, ThemeOfEvent, SubscribeUser


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']

        user = User.objects.filter(email=email)

        if user:
            return Response({'message': 'Пользователь уже есть'}, status.HTTP_403_FORBIDDEN)
        else:
            create_user = User.objects.create_user(email, password, first_name, last_name)

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
    filterset_fields = ('themeOfEvent', 'city', 'formatEvent', 'event_date')


class EventCreateModelViewSet(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data.get('themeOfEvent'))
        return Event.objects.create(
            **data, user_id=request.user.id, themeOfEvent_id=data.get('themeOfEvent')).save()


class EventCreateModelAPIView(CreateAPIView):
    serializer_class = EventCreateSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = request.data

        Event.objects.create(
            user_id=request.user.id,
            title=data['title'],
            description=data['description'],
            address=data['address'],
            event_date=data['event_date'],
            event_time=data['event_time'],
            themeOfEvent_id=data['themeOfEvent'],
            city_id=data['city'],
            formatEvent_id=data['formatEvent']
        ).save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class EventSubscribeReadonlyAPIView(ReadOnlyModelViewSet):
    queryset = SubscribeUser.objects.all()
    serializer_class = EventSubscribeSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('event',)


# class EventSubscribeReadonlyAPIView(GenericAPIView):
#     serializer_class = EventReadonlySubscribeSerializer
#
#     def get(self, request, pk):
#         users = SubscribeUser.objects.filter(event_id=pk)
#
#         serializer = self.serializer_class(data=users, many=True)
#         serializer.is_valid()
#
#         return Response(serializer.data, status.HTTP_200_OK)


class EventDeleteSubscribeAPIView(DestroyAPIView):
    queryset = SubscribeUser.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        user = get_object_or_404(SubscribeUser, event_id=pk, user_id=request.user.id)
        user.delete()

        return Response(pk, status.HTTP_200_OK)


class EventSubscribeModelViewSet(GenericAPIView):
    serializer_class = EventSubscribeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        checkUser = SubscribeUser.objects.filter(user_id=request.user.id, event_id=pk).exists()

        if checkUser:
            return Response({"message": "Такой пользователь уже существует!"}, status.HTTP_400_BAD_REQUEST)

        data = request.data

        event = Event.objects.filter(pk=pk).exists()

        if event is False:
            return Response({'message': 'Такой мероприятии не существует'}, status.HTTP_404_NOT_FOUND)

        subscribe = SubscribeUser(
            user_id=request.user.id,
            event_id=pk,
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        subscribe.save()
        return Response({'message': 'Успешно!'}, status.HTTP_201_CREATED)


class EventUpdateModelViewSet(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id',)
    permission_classes = (IsCheck,)
    lookup_url_kwarg = 'pk'


class EventDestroyAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id',)
    permission_classes = (IsCheck,)
    lookup_url_kwarg = 'pk'


class ThemeReadonlyAPIView(ReadOnlyModelViewSet):
    queryset = ThemeOfEvent.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id',)
    lookup_url_kwarg = 'pk'
