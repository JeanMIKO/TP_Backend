from .user import UtilisateurSerializer, RegisterSerializer
from .etudiant import EtudiantSerializer
from .enseignant import EnseignantSerializer
from .attribution import AttributionSerializer
from .note import NoteSerializer

__all__ = [
    'UtilisateurSerializer', 
    'RegisterSerializer',
    'EtudiantSerializer', 
    'EnseignantSerializer',
    'AttributionSerializer', 
    'NoteSerializer'
]