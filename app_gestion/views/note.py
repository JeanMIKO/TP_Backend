from rest_framework import generics, permissions
from ..models import Note
from ..serializers import NoteSerializer
from ..permissions import IsAdmin, IsEnseignant

class NoteListView(generics.ListAPIView):
    
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Note.objects.select_related('etudiant_id__user', 'enseignant_id__user').all()
        if user.role == 'admin':
            return qs
        if user.role == 'enseignant' and getattr(user, 'enseignant_profile', None):
            return qs.filter(enseignant_id=user.enseignant_profile)
        # Étudiant : interdit ici
        return Note.objects.none()
