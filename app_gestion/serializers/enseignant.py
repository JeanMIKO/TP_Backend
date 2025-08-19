from rest_framework import serializers
from ..models import Enseignant
from .user import UtilisateurSerializer

class EnseignantSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Enseignant
        fields = ['id', 'user', 'user_id', 'specialite']
