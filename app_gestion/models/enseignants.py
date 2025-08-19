from django.db import models
from .user import Utilisateur


class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='enseignant_profile')
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.specialite}"
