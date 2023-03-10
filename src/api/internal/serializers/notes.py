from rest_framework import serializers

from api.internal.models.notes import Note


class NoteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()

    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'created_at')
