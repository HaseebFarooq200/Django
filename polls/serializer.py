from rest_framework import serializers
from .models import Users, Posts, Comment

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            data['email'] = email
            data['password'] = password
        else:
            raise serializers.ValidationError("Both email and password are required")
        return data

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'