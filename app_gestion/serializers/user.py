from rest_framework import serializers
from ..models import Utilisateur, Etudiant, Enseignant

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.ChoiceField(choices=Utilisateur.ROLES)

    class Meta:
        model = Utilisateur
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Utilisateur(**validated_data)
        user.set_password(password)
        user.save()

        
        if user.role == 'etudiant':
            Etudiant.objects.create(user=user)
        elif user.role == 'enseignant':
            Enseignant.objects.create(user=user, specialite='')

        return user
