from django.urls import path
from . import views

urlpatterns = [
    path('mine/', views.ManageSpecializationListView.as_view(), name='manage_specialization_list'),
    path('create/', views.SpecializationCreateView.as_view(), name='specialization_create'),
    path('<pk>/edit/', views.SpecializationUpdateView.as_view(), name='specialization_edit'),
    path('<pk>/delete/', views.SpecializationDeleteView.as_view(), name='specialization_delete'),
    path('<pk>/project/', views.SpecializationProjectUpdateView.as_view(), name='specialization_project_update'),
    path('project/<int:project_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='project_content_create'),
    path('project/<int:project_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(),name='project_content_update'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='project_content_delete'),
    path('project/<int:project_id>/', views.ProjectContentListView.as_view(), name='project_content_list'),
    path('project/order/', views.ProjectOrderView.as_view(), name='project_order'),
    path('content/order/', views.ContentOrderView.as_view(), name='content_order'),
    path('internship/<slug:internship>/', views.SpecializationListView.as_view(), name='specialization_list_internship'),
    path('<slug:slug>/', views.SpecializationDetailView.as_view(), name='specialization_detail'),
]