from django.db import models
from .enseignants import Enseignant
from .etudiants import Etudiant

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notes')
    enseignant_id = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='notes')
    valeur = models.FloatField()
    commentaire = models.TextField(blank=True, null=True)
    date_ajout = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant_id.user.username} - {self.valeur}"