from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from requests import Response
from rest_framework import viewsets, generics
from rest_framework import status

from teamwork.users.api.serializers import EmployeeGetSerializer, EmployeePostSerializer, EmployeeSerializer, EmployerGetSerializer, EmployerPostSerializer, UserSerializer,UserDetailSerializer
from teamwork.users.models import Employee, Employer
User = get_user_model()

class UsersViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UsersViewDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class ForEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ForEmployer(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerPostSerializer
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return EmployerGetSerializer
        return EmployerPostSerializer
    
    # def create(self, request, *args, **kwargs):
    #     serializer = EmployerPostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user=self.request.user) # user pole ni zapros berayotgan user bn tuldiradi
    #     return Response(serializer.data)

class ForEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeePostSerializer
    
    def get_serializer_class(self):
        if self.action in ['list']:
            return EmployeeGetSerializer
        return EmployeePostSerializer

# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     slug_field = "phone"
#     slug_url_kwarg = "phone"



# user_detail_view = UserDetailView.as_view()


# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = User
#     fields = ["name"]
#     success_message = _("Information successfully updated")

#     def get_success_url(self):
#         assert (
#             self.request.user.is_authenticated
#         )  # for mypy to know that the user is authenticated
#         return self.request.user.get_absolute_url()

#     def get_object(self):
#         return self.request.user


# user_update_view = UserUpdateView.as_view()


# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False

#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"phone": self.request.user.phone})


# user_redirect_view = UserRedirectView.as_view()
