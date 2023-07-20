from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .serializers import UserDetailSerializer, UserSerializer, UserUpdateSerializer, UserCreateSerializer

User = get_user_model()


# class UsersApiView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
#     def get(self, request, *args, **kwargs):
#         user = self.get_queryset()
#         serializer = self.get_serializer(user, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class UserDetailApiView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
    

# class UserUpdateApiView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserUpdateSerializer

# class UserCreateApiView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

# class UserDeleteApiView(DestroyAPIView):
#     queryset = User.objects.all()


# user_api_view = UsersApiView.as_view()
# user_detail_view = UserDetailApiView.as_view()
# user_update_api_view = UserUpdateApiView.as_view()
# user_delete_api_view = UserDeleteApiView.as_view()
# user_create_api_view = UserCreateApiView.as_view()


# class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "username"

#     def get_queryset(self, *args, **kwargs):
#         assert isinstance(self.request.user.id, int)
#         return self.queryset.filter(id=self.request.user.id)

#     @action(detail=False)
#     def me(self, request):
#         serializer = UserSerializer(request.user, context={"request": request})
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
