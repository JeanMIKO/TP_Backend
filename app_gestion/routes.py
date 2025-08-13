
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentification
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Toutes les routes concernant Etudiants
    path('etudiants/', views.EtudiantListCreateView.as_view(), name='etudiant-list-create'),
    path('etudiants/<int:pk>/', views.EtudiantRetrieveUpdateDestroyView.as_view(), name='etudiant-detail'),
    path('etudiants/<int:pk>/theme/', views.UpdateThemeView.as_view(), name='update-theme'),
    path('etudiants/<int:pk>/notes/', views.StudentNotesView.as_view(), name='student-notes'),

    # Toutes les routes concernant Enseignants
    path('enseignants/', views.EnseignantListCreateView.as_view(), name='enseignant-list-create'),
    path('enseignants/<int:pk>/', views.EnseignantRetrieveUpdateDestroyView.as_view(), name='enseignant-detail'),
    path('enseignants/<int:pk>/etudiants/', views.TeacherStudentsView.as_view(), name='teacher-students'),
    path('enseignants/<int:pk>/noter/', views.TeacherNoteStudentView.as_view(), name='teacher-note'),

    # Les routes concernant Attributions
    path('attributions/', views.AttributionListCreateView.as_view(), name='attribution-list-create'),
    path('attributions/<int:pk>/', views.AttributionRetrieveUpdateDestroyView.as_view(), name='attribution-detail'),

    # routes concernant Notes
    path('notes/', views.NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyView.as_view(), name='note-detail'),
]
