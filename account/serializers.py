from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.models import Doctor
from .models import Appointment

# class AppointmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'



from account import models
User = get_user_model()
class RegistrationDoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = Doctor
        fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                'Passwords must be the same'
            )
        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'The password must contain letters and numbers'
            )
        return attrs

    def create(self, validated_data):
        user = Doctor.objects.create_user(**validated_data)
        return user


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                'Passwords must be the same'
            )
        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'The password must contain letters and numbers'
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.code = attrs['code']
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ''
            user.save()
        except:
            raise serializers.ValidationError('неверный код')

class ActivationDoctorSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.code = attrs['code']
        return attrs

    def save(self, **kwargs):
        try:
            user = Doctor.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ''
            user.save()
        except:
            raise serializers.ValidationError('неверный код')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ('password',)
    # address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20, null=True)
#     department = models.CharField(max_length=50, choices=departments, default='Cardiologist')
#     status = models.BooleanField(default=False)
#
#     class RegistrationSerializer(serializers.ModelSerializer):
#         password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
#         password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True)
#
#         class Meta:
#             model = User
#             fields = ('email', 'password', 'password_confirmation', 'first_name', 'last_name', 'username', 'avatar')
#
#         def validate(self, attrs):
#             password = attrs['password']
#             password_confirmation = attrs.pop('password_confirmation')
#             if password != password_confirmation:
#                 raise serializers.ValidationError(
#                     'Passwords must be the same'
#                 )
#             if password.isdigit() or password.isalpha():
#                 raise serializers.ValidationError(
#                     'The password must contain letters and numbers'
#                 )
#             return attrs
#
#         def create(self, validated_data):
#             user = User.objects.create_user(**validated_data)
#             return user
#
# #         model = User
# #         exclude = ('password',)