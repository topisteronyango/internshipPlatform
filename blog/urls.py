from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('postlistblog/', views.PostList.as_view(), name='post_list_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)