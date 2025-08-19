from django.db import models
from .user import Utilisateur


class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='etudiant_profile')
    theme_memoire = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
