from django.urls import include, path

from teamwork.users.views import ForEmployee, ForEmployer, UsersViewList,UsersViewDetail
# from teamwork.users.api.views import (
#     user_api_view, 
#     user_detail_view, 
#     user_update_api_view, 
#     user_delete_api_view,
#     user_create_api_view
#     )

# from teamwork.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )
from rest_framework import routers

app_name = "users"

router = routers.DefaultRouter()
router.register(r'foremployee', ForEmployee, basename='foremployee')
router.register(r'foremployer', ForEmployer, basename='foremployer')

urlpatterns = [
    path('', UsersViewList.as_view()),
    path('<int:pk>/', UsersViewDetail.as_view()),
    path('', include(router.urls))

]

# urlpatterns = [
#     path('', view=UsersViewList, name='users'),
#     # path('detail/<int:pk>/', view=user_detail_view, name='user_detail'),
#     # path('update/<int:pk>/', view=user_update_api_view, name='user_update'),
#     # path('delete/<int:pk>/', view=user_delete_api_view, name='user_delete'),
#     # path('create/', view=user_create_api_view, name='user_create'),

#     # path("~redirect/", view=user_redirect_view, name="redirect"),
#     # path("~update/", view=user_update_view, name="update"),
#     # path("<str:username>/", view=user_detail_view, name="detail"),
# ]
