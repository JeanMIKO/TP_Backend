from django.urls import path
from .views import (
    RegisterView,
    EtudiantListCreateView, EtudiantRetrieveUpdateDestroyView, 
    UpdateThemeView, StudentNotesView,
    EnseignantListCreateView, EnseignantRetrieveUpdateDestroyView,
    TeacherStudentsView, TeacherNoteStudentView,
    AttributionListCreateView, AttributionRetrieveUpdateDestroyView,
    NoteListCreateView, NoteRetrieveUpdateDestroyView
)

urlpatterns = [
    # Création d'un compte utilisateur 
    path('register/', RegisterView.as_view(), name='register'),

    path('etudiants/', EtudiantListCreateView.as_view(), name='etudiant-list-create'),
    path('etudiants/<int:pk>/', EtudiantRetrieveUpdateDestroyView.as_view(), name='etudiant-detail'),
    path('etudiants/<int:pk>/theme/', UpdateThemeView.as_view(), name='update-theme'),
    path('etudiants/<int:pk>/notes/', StudentNotesView.as_view(), name='student-notes'),

    path('enseignants/', EnseignantListCreateView.as_view(), name='enseignant-list-create'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyView.as_view(), name='enseignant-detail'),
    path('enseignants/<int:pk>/etudiants/', TeacherStudentsView.as_view(), name='teacher-students'),
    path('enseignants/<int:pk>/noter/', TeacherNoteStudentView.as_view(), name='teacher-note'),

    path('attributions/', AttributionListCreateView.as_view(), name='attribution-list-create'),
    path('attributions/<int:pk>/', AttributionRetrieveUpdateDestroyView.as_view(), name='attribution-detail'),

    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
]


