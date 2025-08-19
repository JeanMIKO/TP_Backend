from rest_framework import viewsets
from ..serializers import EtudiantSerializer
from ..models import Etudiant

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer