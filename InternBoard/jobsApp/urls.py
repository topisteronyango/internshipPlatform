from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jobsApp'

urlpatterns = [
    path('', views.joblist, name="job-list"), # reverse("jobs:job_list")
    path('job-detail/<str:slug>', views.job_detail, name="job-detail"),
    path('add-job', views.add_job, name="add-job"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)