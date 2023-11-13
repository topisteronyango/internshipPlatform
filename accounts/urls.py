from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views



# from accounts import views as accounts_views
# from . import views
app_name='accounts'

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset.html',
        email_template_name='password/password_reset_email.html',
        subject_template_name='password/password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/finish/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_finish.html'), name='password_reset_finish'),
    path('reset/confirm/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirming.html'),
        name='password_reset_confirming'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
        name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password/password_change.html'),
    name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password/password_change_done.html'),
    name='password_change_done'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='myaccount'),

    
]

# app_name='job'

# urlpatterns = [
#     path('signup/',views.signup , name='signup'),
#     path('profile/',views.profile , name='profile'),
#     path('profile/edit',views.profile_edit , name='profile_edit'),
# ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)