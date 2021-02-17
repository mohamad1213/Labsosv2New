from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

# app_name ='accounts',

urlpatterns = [
    path('', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
    path('profile/', views.accountSettings, name="profile"),
    path('profile_staf/', views.accountSettings_staf, name="profile_staf"),
    path('profile_dosen/', views.accountSettings_dosen, name="profile_dosen"),
    path('input/', views.edit, name="edit"),
    
	# path('<id>/', views.detail),
    # path('<id>/delete/', views.delete),
    # path('<id>/update/', views.delete),
]