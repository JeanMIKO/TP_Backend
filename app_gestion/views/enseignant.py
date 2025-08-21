from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Enseignant, Etudiant, Attribution, Note
from ..serializers import EnseignantSerializer, EtudiantSerializer, NoteSerializer

class EnseignantListCreateView(generics.ListCreateAPIView):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.select_related('user').all()
    permission_classes = [permissions.AllowAny]

class EnseignantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()
    permission_classes = [permissions.AllowAny]

class TeacherStudentsView(generics.ListAPIView):
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        ens = get_object_or_404(Enseignant, pk=pk)
        atts = Attribution.objects.filter(enseignant_id=ens)
        etudiants = Etudiant.objects.filter(attributions__in=atts).distinct()
        serializer = self.get_serializer(etudiants, many=True)
        return Response(serializer.data)

class TeacherNoteStudentView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        ens = get_object_or_404(Enseignant, pk=pk)

        etudiant_pk = request.data.get('etudiant_id')
        if not etudiant_pk:
            return Response({'detail': 'etudiant_id requis'}, status=status.HTTP_400_BAD_REQUEST)

        etu = get_object_or_404(Etudiant, pk=etudiant_pk)

        serializer = self.get_serializer(data={
            'etudiant_id': etu.pk,
            'enseignant_id': ens.pk,
            'valeur': request.data.get('valeur'),
            'commentaire': request.data.get('commentaire', '')
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
