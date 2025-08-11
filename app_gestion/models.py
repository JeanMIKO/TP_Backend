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


class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='etudiant_profile')
    theme_memoire = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='enseignant_profile')
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.specialite}"


class Attribution(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='attributions')
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='attributions')
    date_attribution = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('etudiant_id', 'enseignant_id')

    def __str__(self):
        return f"{self.etudiant_id.user.username} → {self.enseignant_id.user.username}"


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notes')
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='notes')
    valeur = models.FloatField()
    commentaire = models.TextField(blank=True, null=True)
    date_ajout = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant_id.user.username} - {self.valeur}"

