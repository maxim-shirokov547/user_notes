from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.internal.views.auth import SignInView, LogOutView
from api.internal.views.notes import NoteViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet, basename='notes')


urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
]

urlpatterns += router.urls
