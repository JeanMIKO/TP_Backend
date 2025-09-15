from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator
class Utilisateur(AbstractUser):
    ROLES = (
        ('admin', 'Administrateur'),
        ('etudiant', 'Étudiant'),
        ('enseignant', 'Enseignant'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',)
    )
    sexe = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)        
    age = models.PositiveIntegerField(validators=[MinValueValidator(15)],  null=True,blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    groups = models.ManyToManyField(Group, related_name='jean_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='jean_permissions', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
