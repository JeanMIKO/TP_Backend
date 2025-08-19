from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Utilisateur(AbstractUser):
    ROLES = (
        ('admin', 'Administrateur'),
        ('etudiant', 'Étudiant'),
        ('enseignant', 'Enseignant'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    groups = models.ManyToManyField(
        Group,
        related_name='jean_groups', 
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='jean_permissions', 
        blank=True
    )