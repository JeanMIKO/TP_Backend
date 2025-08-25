from django.db import models
from .etudiant import Etudiant
from .enseignant import Enseignant

class Attribution(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='attributions')
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='attributions')
    date_attribution = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['etudiant_id'], name='unique_advisor_per_student')
        ]

    def __str__(self):
        return f"{self.etudiant_id.user.username} → {self.enseignant_id.user.username}"
