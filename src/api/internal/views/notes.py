from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from api.internal.models.notes import Note
from api.internal.serializers.notes import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)
    serializer_class = NoteSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user.id)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
