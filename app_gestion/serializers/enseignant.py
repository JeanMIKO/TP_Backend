from rest_framework import serializers
from ..models import Enseignant
from .user import UtilisateurSerializer

class EnseignantSerializer(serializers.ModelSerializer):
    user = UtilisateurSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Enseignant
        fields = ['id', 'user', 'user_id', 'specialite']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            from ..models import Utilisateur
            user = Utilisateur.objects.get(pk=user_id)
            if user.role != 'enseignant':
                raise serializers.ValidationError("Le rôle du user doit être 'enseignant'.")
            return Enseignant.objects.create(user=user, **validated_data)
        return super().create(validated_data)
