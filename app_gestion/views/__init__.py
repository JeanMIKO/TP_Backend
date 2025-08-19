from .user import RegisterView
from .etudiant import (
    EtudiantListCreateView,
    EtudiantRetrieveUpdateDestroyView,
    UpdateThemeView,
    StudentNotesView,
)
from .enseignant import (
    EnseignantListCreateView,
    EnseignantRetrieveUpdateDestroyView,
    TeacherStudentsView,
    TeacherNoteStudentView,
)
from .attribution import (
    AttributionListCreateView,
    AttributionRetrieveUpdateDestroyView,
)
from .note import (
    NoteListCreateView,
    NoteRetrieveUpdateDestroyView,
)

__all__ = [
    "RegisterView",
    "EtudiantListCreateView",
    "EtudiantRetrieveUpdateDestroyView",
    "UpdateThemeView",
    "StudentNotesView",
    "EnseignantListCreateView",
    "EnseignantRetrieveUpdateDestroyView",
    "TeacherStudentsView",
    "TeacherNoteStudentView",
    "AttributionListCreateView",
    "AttributionRetrieveUpdateDestroyView",
    "NoteListCreateView",
    "NoteRetrieveUpdateDestroyView",
]
