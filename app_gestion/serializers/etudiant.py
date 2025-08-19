from rest_framework import serializers
from ..models import Etudiant
from .user import UtilisateurSerializer

class EtudiantSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Etudiant
        fields = ['id', 'user', 'user_id', 'theme_memoire']
