from .user import RegisterView
from .etudiant import (
    EtudiantListCreateView, EtudiantRetrieveUpdateDestroyView,
    UpdateThemeView, StudentNotesView, EtudiantAdvisorView
)
from .enseignant import (
    EnseignantListCreateView, EnseignantRetrieveUpdateDestroyView,
    TeacherStudentsView, TeacherNoteStudentView
)
from .attribution import AttributionListCreateView, AttributionRetrieveUpdateDestroyView
from .note import NoteListView
