from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

from django.contrib.auth.password_validation import validate_password


 
#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # fields = '__all__'
    fields = ["id", "username", "first_name", "last_name","email",'date_of_birth','language','user_name','phone_number']


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('user_name', 'password', 'password2',
         'email', 'first_name', 'last_name','date_of_birth','language','phone_number')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }


  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
    
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['email'],
     
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      user_name = validated_data['user_name'],
      date_of_birth = validated_data['date_of_birth'],
      language = validated_data['language'],
      phone_number= validated_data['phone_number']


    )
    user.set_password(validated_data['password'])
    user.save()
    return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
