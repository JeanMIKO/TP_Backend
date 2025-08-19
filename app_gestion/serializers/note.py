from rest_framework import serializers
from ..models import Note, Etudiant, Enseignant
from .etudiant import EtudiantSerializer
from .enseignant import EnseignantSerializer

class NoteSerializer(serializers.ModelSerializer):
    etudiant_id = serializers.PrimaryKeyRelatedField(queryset=Etudiant.objects.all())
    enseignant_id = serializers.PrimaryKeyRelatedField(queryset=Enseignant.objects.all())
    etudiant = EtudiantSerializer(source='etudiant_id', read_only=True)
    enseignant = EnseignantSerializer(source='enseignant_id', read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'etudiant_id', 'enseignant_id', 'etudiant', 'enseignant', 'valeur', 'commentaire', 'date_ajout']
        read_only_fields = ['date_ajout']
