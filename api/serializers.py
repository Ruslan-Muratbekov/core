from rest_framework import serializers

from event.models import Event, ThemeOfEvent, SubscribeUser
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'created_at',
            'updated_at',
            'title',
            'description',
            'address',
            'event_date',
            'event_time',
            'themeOfEvent',
            'formatEvent',
            'city',
        ]


class EventReadonlySubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeUser
        fields = '__all__'


class EventSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeUser
        fields = '__all__'
        # fields = [
        #     "first_name",
        #     "last_name",
        # ]


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'address',
            'event_date',
            'event_time',
            'themeOfEvent',
            'formatEvent',
            'city',
        ]


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeOfEvent
        fields = '__all__'
