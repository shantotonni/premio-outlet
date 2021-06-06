from rest_framework.generics import UpdateAPIView
from rest_framework import generics,mixins
from rest_framework.authtoken.models import Token
from .serializers import ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token 
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # return new token
        return Response({'token': token.key}, status=status.HTTP_200_OK)


