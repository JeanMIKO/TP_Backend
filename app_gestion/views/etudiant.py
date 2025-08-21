from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Etudiant, Note, Attribution, Enseignant
from ..serializers import EtudiantSerializer, NoteSerializer

class EtudiantListCreateView(generics.ListCreateAPIView):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.select_related("user").all()
    permission_classes = [permissions.AllowAny]

class EtudiantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()
    permission_classes = [permissions.AllowAny]

class UpdateThemeView(generics.UpdateAPIView):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()
    permission_classes = [permissions.AllowAny]

    def patch(self, request, *args, **kwargs):
        etu = self.get_object()
        theme = request.data.get('theme_memoire', None)
        if theme is None:
            return Response({'detail': 'theme_memoire required'}, status=status.HTTP_400_BAD_REQUEST)
        etu.theme_memoire = theme
        etu.save()
        return Response(self.get_serializer(etu).data)

class StudentNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        etu = get_object_or_404(Etudiant, pk=pk)
        return Note.objects.filter(etudiant_id=etu)
