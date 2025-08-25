from rest_framework import serializers
from ..models import Etudiant
from .user import UtilisateurSerializer

class EtudiantSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Etudiant
        fields = ['id', 'user', 'user_id', 'theme_memoire']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            from ..models import Utilisateur
            user = Utilisateur.objects.get(pk=user_id)
            if user.role != 'etudiant':
                raise serializers.ValidationError("Le rôle du user doit être 'etudiant'.")
            return Etudiant.objects.create(user=user, **validated_data)
        return super().create(validated_data)
