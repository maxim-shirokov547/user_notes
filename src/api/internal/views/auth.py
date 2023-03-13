from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.internal.serializers.auth import LogOutSerializer, SignUpSerializer


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer
    swagger_tags = ['auth']


class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    @swagger_auto_schema(request_body=LogOutSerializer, tags=['auth'])
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                token = RefreshToken(request.data.get('refresh'))
                token.blacklist()
            except TokenError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    swagger_tags = ['auth']


class RefreshTokenView(TokenRefreshView):
    swagger_tags = ['auth']
