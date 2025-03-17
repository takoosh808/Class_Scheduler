from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["username", "password"]
        extra_kwargs = {'password': {'write_only': True}}

     def create(self, validated_data):
        user = Student(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
