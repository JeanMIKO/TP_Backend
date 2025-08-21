from rest_framework import generics, permissions, status
from rest_framework.response import Response

from ..models import Note, Enseignant, Etudiant
from ..serializers import NoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.select_related('notes').all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        qs = Note.objects.all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [permissions.AllowAny]
