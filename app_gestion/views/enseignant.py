from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Enseignant, Etudiant, Note, Attribution
from ..serializers import EnseignantSerializer, EtudiantSerializer, NoteSerializer
from ..permissions import IsAdmin, IsEnseignant

class EnseignantListCreateView(generics.ListCreateAPIView):
    serializer_class = EnseignantSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    queryset = Enseignant.objects.select_related('user').all()
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'specialite']
    ordering_fields = ['id', 'user__username', 'specialite']

class EnseignantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnseignantSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Enseignant.objects.select_related('user').all()

    def get_object(self):
        obj = super().get_object()
        # Admin : OK ; Enseignant : peut voir/modifier seulement son profil
        user = self.request.user
        if user.role == 'admin':
            return obj
        if user.role == 'enseignant' and getattr(user, 'enseignant_profile', None):
            if obj.pk == user.enseignant_profile.pk:
                return obj
        self.permission_denied(self.request, message="Accès refusé.")
        return obj

class TeacherStudentsView(generics.ListAPIView):
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnseignant]
    pagination_class = None

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        # Un enseignant ne peut lister que ses étudiants
        if not getattr(self.request.user, 'enseignant_profile', None) or self.request.user.enseignant_profile.pk != pk:
            return Etudiant.objects.none()
        ens = get_object_or_404(Enseignant.objects.select_related('user'), pk=pk)
        return Etudiant.objects.select_related('user').filter(attributions__enseignant_id=ens).distinct()

class TeacherNoteStudentView(generics.CreateAPIView):
    
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnseignant]

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk') 
        # Vérifie que l’enseignant authentifié correspond
        if not getattr(request.user, 'enseignant_profile', None) or request.user.enseignant_profile.pk != int(pk):
            return Response({'detail': 'Accès refusé.'}, status=status.HTTP_403_FORBIDDEN)

        etudiant_pk = request.data.get('etudiant_id')
        if not etudiant_pk:
            return Response({'detail': 'etudiant_id requis'}, status=status.HTTP_400_BAD_REQUEST)

        ens = request.user.enseignant_profile
        etu = get_object_or_404(Etudiant, pk=etudiant_pk)

        # Vérifie l’attribution avant de créer la note
        if not Attribution.objects.filter(etudiant_id=etu, enseignant_id=ens).exists():
            return Response({'detail': "L'étudiant n'est pas attribué à cet enseignant."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={
            'etudiant_id': etu.pk,
            'enseignant_id': ens.pk,
            'valeur': request.data.get('valeur'),
            'commentaire': request.data.get('commentaire', '')
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
