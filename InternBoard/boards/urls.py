from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'boards'

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<pk>/', views.board_topics, name='board_topics'),
    path('boards/<pk>/new/', views.new_topic, name='new_topic'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)