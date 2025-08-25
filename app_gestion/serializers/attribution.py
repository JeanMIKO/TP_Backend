from rest_framework import serializers
from ..models import Attribution, Etudiant, Enseignant

class AttributionDetailSerializer(serializers.ModelSerializer):
    etudiant = serializers.SerializerMethodField()
    enseignant = serializers.SerializerMethodField()

    class Meta:
        model = Attribution
        fields = ['id', 'etudiant', 'enseignant', 'date_attribution']

    def get_etudiant(self, obj):
        return {
            "id": obj.etudiant_id.id,
            "username": obj.etudiant_id.user.username,
            "theme_memoire": obj.etudiant_id.theme_memoire,
        }

    def get_enseignant(self, obj):
        return {
            "id": obj.enseignant_id.id,
            "username": obj.enseignant_id.user.username,
            "specialite": obj.enseignant_id.specialite,
        }

class AttributionSerializer(serializers.ModelSerializer):
    etudiant_id = serializers.PrimaryKeyRelatedField(queryset=Etudiant.objects.all())
    enseignant_id = serializers.PrimaryKeyRelatedField(queryset=Enseignant.objects.all())
    etudiant = AttributionDetailSerializer(source='*', read_only=True)
    enseignant = AttributionDetailSerializer(source='*', read_only=True)

    class Meta:
        model = Attribution
        fields = ['id', 'etudiant_id', 'enseignant_id', 'etudiant', 'enseignant', 'date_attribution']
        read_only_fields = ['date_attribution']

    def validate(self, attrs):
        etu: Etudiant = attrs['etudiant_id']
        ens: Enseignant = attrs['enseignant_id']
        theme = (etu.theme_memoire or "").lower()
        specialite = (ens.specialite or "").lower()

        if not theme:
            raise serializers.ValidationError("L'étudiant n'a pas de thème de mémoire défini.")
        if not specialite:
            raise serializers.ValidationError("L'enseignant n'a pas de spécialité définie.")
        if specialite not in theme:
            raise serializers.ValidationError(
                "Incompatibilité: la spécialité de l'enseignant ne correspond pas au thème de l'étudiant."
            )
        return attrs
