from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['who', 'username', 'first_name', 'last_name', 'phone', 'email', 'password', 'avatar']
        fields = ['name', 'phone', 'type', 'image', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
                        name=self.validated_data['name'],
                        phone=self.validated_data['phone'],
                        type=self.validated_data['type'],
                        image=self.validated_data['image'],
                        )

        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user