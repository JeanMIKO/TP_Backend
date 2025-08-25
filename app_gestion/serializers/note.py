from rest_framework import serializers
from ..models import Note, Etudiant, Enseignant

class NoteSerializer(serializers.ModelSerializer):
    etudiant_id = serializers.PrimaryKeyRelatedField(queryset=Etudiant.objects.all())
    enseignant_id = serializers.PrimaryKeyRelatedField(queryset=Enseignant.objects.all())

    class Meta:
        model = Note
        fields = ['id', 'etudiant_id', 'enseignant_id', 'valeur', 'commentaire', 'date_ajout']
        read_only_fields = ['date_ajout']

    def validate(self, attrs):
        etu = attrs['etudiant_id']
        ens = attrs['enseignant_id']
        
        if not etu.attributions.filter(enseignant_id=ens).exists():
            raise serializers.ValidationError("Cet étudiant n'est pas attribué à cet enseignant.")
        return attrs
