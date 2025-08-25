from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Etudiant, Note, Attribution
from ..serializers import EtudiantSerializer, NoteSerializer
from ..permissions import IsAdmin, IsEtudiant

class EtudiantListCreateView(generics.ListCreateAPIView):
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    queryset = Etudiant.objects.select_related('user').all()
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'theme_memoire']
    ordering_fields = ['id', 'user__username']

class EtudiantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Etudiant.objects.select_related('user').all()

    def get_object(self):
        obj = super().get_object()
        # Admin : accès total ; Étudiant : seulement son propre profil
        user = self.request.user
        if user.role == 'admin':
            return obj
        if user.role == 'etudiant' and getattr(user, 'etudiant_profile', None):
            if obj.pk == user.etudiant_profile.pk:
                return obj
        # Enseignant n'a pas accès à modifier/supprimer un étudiant
        self.permission_denied(self.request, message="Accès refusé.")
        return obj  # non atteint

class UpdateThemeView(generics.UpdateAPIView):
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated, IsEtudiant]
    queryset = Etudiant.objects.select_related('user').all()

    def patch(self, request, *args, **kwargs):
        etu = self.get_object()
        # L'étudiant ne peut mettre à jour QUE son propre thème
        if request.user.etudiant_profile.pk != etu.pk:
            return Response({'detail': 'Accès refusé.'}, status=status.HTTP_403_FORBIDDEN)

        theme = request.data.get('theme_memoire')
        if theme is None:
            return Response({'detail': 'theme_memoire requis'}, status=status.HTTP_400_BAD_REQUEST)
        etu.theme_memoire = theme
        etu.save()
        return Response(self.get_serializer(etu).data)

class StudentNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None  

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        # Étudiant : uniquement soi-même ; Admin : oui
        if self.request.user.role == 'etudiant':
            if self.request.user.etudiant_profile.pk != pk:
                return Note.objects.none()
        return Note.objects.select_related('etudiant_id__user', 'enseignant_id__user').filter(etudiant_id__pk=pk)

class EtudiantAdvisorView(generics.RetrieveAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = None  

    def get(self, request, *args, **kwargs):
        etu_pk = kwargs.get('pk')
        etu = get_object_or_404(Etudiant.objects.select_related('user'), pk=etu_pk)

        # Étudiant : ne voir que son assignation ; Admin : oui ; Enseignant: non
        if request.user.role == 'etudiant' and request.user.etudiant_profile.pk != etu.pk:
            return Response({'detail': 'Accès refusé.'}, status=status.HTTP_403_FORBIDDEN)
        if request.user.role == 'enseignant':
            return Response({'detail': 'Accès refusé.'}, status=status.HTTP_403_FORBIDDEN)

        attribution = Attribution.objects.select_related('enseignant_id__user').filter(etudiant_id=etu).first()
        if not attribution:
            return Response({'detail': 'Aucun maître de mémoire attribué.'}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'etudiant': {'id': etu.id, 'username': etu.user.username, 'theme_memoire': etu.theme_memoire},
            'enseignant': {
                'id': attribution.enseignant_id.id,
                'username': attribution.enseignant_id.user.username,
                'specialite': attribution.enseignant_id.specialite,
            },
            'date_attribution': attribution.date_attribution
        }
        return Response(data)
