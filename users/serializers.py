from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'phone_number', 'password', 'password2',]
        extra_kwargs = {
            'password': {
                'write_only':True
            },
            'password2': {
                'write_only':True
            }
        }

    def save(self, request):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'email', 'phone_number','is_active']
        read_only_fields = ('usernam','email','is_active')
      
 