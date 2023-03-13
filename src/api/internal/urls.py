from django.urls import path
from rest_framework import routers

from api.internal.views.auth import LoginView, LogOutView, RefreshTokenView, SignUpView
from api.internal.views.notes import NoteViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet, basename='notes')


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
]

urlpatterns += router.urls
