from django.urls import path
from teamwork.skills.views import (SkillApiView, SpecialtiesApiView)

app_name = "skills"
urlpatterns = [
    path('', SkillApiView.as_view(), name='skills'),
    path('special/', SpecialtiesApiView.as_view(), name='special'),
]

