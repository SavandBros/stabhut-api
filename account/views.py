from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from account.serializers import UserSerializer
from api.v1.utils import IsOwnerOrReadOnly, StandardPagination


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    pagination_class = StandardPagination
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = "username"


def jwt_response_payload_handler(token, user=None, request=None) -> dict:
    return {"token": token, "user": UserSerializer(user, context={"request": request}).data}
