from django.urls import path
from rest_framework import routers

from api.internal.views.auth import LoginView, LogOutView, RefreshTokenView, SignInView
from api.internal.views.notes import NoteViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet, basename='notes')


urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
]

urlpatterns += router.urls
