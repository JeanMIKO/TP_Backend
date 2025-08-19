from rest_framework import serializers
from ..models import Attribution, Etudiant, Enseignant
from .etudiant import EtudiantSerializer
from .enseignant import EnseignantSerializer

class AttributionSerializer(serializers.ModelSerializer):
    etudiant_id = serializers.PrimaryKeyRelatedField(queryset=Etudiant.objects.all())
    enseignant_id = serializers.PrimaryKeyRelatedField(queryset=Enseignant.objects.all())
    etudiant = EtudiantSerializer(source='etudiant_id', read_only=True)
    enseignant = EnseignantSerializer(source='enseignant_id', read_only=True)

    class Meta:
        model = Attribution
        fields = ['id', 'etudiant_id', 'enseignant_id', 'etudiant', 'enseignant', 'date_attribution']
