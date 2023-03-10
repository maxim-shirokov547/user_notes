from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from api.internal.serializers.auth import LogOutSerializer, SignInSerializer


class SignInView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer


class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                token = RefreshToken(request.data.get('refresh'))
                token.blacklist()
            except TokenError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)
