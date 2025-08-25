from rest_framework import generics, permissions
from ..models import Attribution
from ..serializers import AttributionSerializer
from ..permissions import IsAdmin

class AttributionListCreateView(generics.ListCreateAPIView):
    serializer_class = AttributionSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    queryset = Attribution.objects.select_related('etudiant_id__user', 'enseignant_id__user').all()
    search_fields = ['etudiant_id__user__username', 'enseignant_id__user__username', 'enseignant_id__specialite']
    ordering_fields = ['date_attribution']

class AttributionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributionSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    queryset = Attribution.objects.select_related('etudiant_id__user', 'enseignant_id__user').all()
