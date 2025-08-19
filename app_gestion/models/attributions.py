from django.db import models
from .etudiants import Etudiant
from .enseignants import Enseignant



class Attribution(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='attributions')
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='attributions')
    date_attribution = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('etudiant_id', 'enseignant_id')

    def __str__(self):
        return f"{self.etudiant_id.user.username} → {self.enseignant_id.user.username}"