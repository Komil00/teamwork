from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from teamwork.skills.models import Skills, Specialties
from teamwork.skills.serializers import SkillsSerializer, GetSkillsSerializer, SpecialSerializer


class SkillApiView(ListAPIView):
    queryset = Skills.objects.filter(is_moderated=True)
    serializer_class = GetSkillsSerializer
    
    def get(self, request, *args, **kwargs):
        skills = self.get_queryset()
        serializer = self.get_serializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SpecialtiesApiView(ListAPIView):
    queryset = Specialties.objects.filter(parent=None)
    serializer_class = SpecialSerializer
    
    def get(self, request, *args, **kwargs):
        skills = self.get_queryset()
        serializer = self.get_serializer(skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#Seriliazer
#ApiView
#View.Set
#Rest filtering searching, pagenation
#action
