from rest_framework.permissions import BasePermission
from event.models import Event


class IsCheck(BasePermission):
    def has_permission(self, request, view):
        pk = request.parser_context['kwargs']['pk']
        userID = request.auth.payload['user_id']
        event = Event.objects.filter(pk=pk)
        if event.exists():
            return bool(request.user and request.user.is_authenticated and event[0].user_id == userID)

        return False
