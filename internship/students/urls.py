from django.urls import path
from . import views
urlpatterns = [
 path('register/', views.StudentRegistrationView.as_view(), name='student_registration'),
 path('enroll-specialization/', views.StudentEnrollSpecializationView.as_view(), name='student_enroll_specialization'),
 path('specializations/', views.StudentSpecializationListView.as_view(), name='student_specialization_list'),
 path('specialization/<pk>/', views.StudentSpecializationDetailView.as_view(), name='student_specialization_detail'),
 path('specialization/<pk>/<project_id>/', views.StudentSpecializationDetailView.as_view(), name='student_specialization_detail_project'),
]
