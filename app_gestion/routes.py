from django.urls import path
from .views import (
    RegisterView,

    EtudiantListCreateView, EtudiantRetrieveUpdateDestroyView,
    UpdateThemeView, StudentNotesView, EtudiantAdvisorView,

    EnseignantListCreateView, EnseignantRetrieveUpdateDestroyView,
    TeacherStudentsView, TeacherNoteStudentView,

    AttributionListCreateView, AttributionRetrieveUpdateDestroyView,

    NoteListView,  
)

urlpatterns = [
    # Authentification
    path('register/', RegisterView.as_view(), name='register'),

    # Étudiants
    path('etudiants/', EtudiantListCreateView.as_view(), name='etudiant-list-create'),
    path('etudiants/<int:pk>/', EtudiantRetrieveUpdateDestroyView.as_view(), name='etudiant-detail'),
    path('etudiants/<int:pk>/theme/', UpdateThemeView.as_view(), name='update-theme'),
    path('etudiants/<int:pk>/notes/', StudentNotesView.as_view(), name='student-notes'),
    path('etudiants/<int:pk>/advisor/', EtudiantAdvisorView.as_view(), name='student-advisor'),

    # Enseignants
    path('enseignants/', EnseignantListCreateView.as_view(), name='enseignant-list-create'),
    path('enseignants/<int:pk>/', EnseignantRetrieveUpdateDestroyView.as_view(), name='enseignant-detail'),
    path('enseignants/<int:pk>/students/', TeacherStudentsView.as_view(), name='teacher-students'),
    path('enseignants/<int:pk>/note-student/', TeacherNoteStudentView.as_view(), name='teacher-note-student'),

    # Attributions (admin)
    path('attributions/', AttributionListCreateView.as_view(), name='attribution-list-create'),
    path('attributions/<int:pk>/', AttributionRetrieveUpdateDestroyView.as_view(), name='attribution-detail'),

    # Notes (consultation)
    path('notes/', NoteListView.as_view(), name='note-list'),
]
