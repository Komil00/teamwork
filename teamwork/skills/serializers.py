from rest_framework import serializers
from teamwork.skills.models import Skills, Specialties

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialties 
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'parent']


class SkillsSerializer(serializers.ModelSerializer):
    special = SpecialSerializer(read_only=True, many=True)
    class Meta:
        model = Skills 
        fields = ['id', 'name', 'special']

class GetSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills 
        fields = ['id', 'name']