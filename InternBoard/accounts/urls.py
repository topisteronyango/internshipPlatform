from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='job'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('profile',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)