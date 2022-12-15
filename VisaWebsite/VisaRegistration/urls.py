from django.urls import path
from django.contrib.auth.views import LogoutView
from VisaRegistration import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('get_visa/', views.VisaView.as_view(template_name='main/visa_processing.html'), name='visa'),
    path('profile/', views.UserProfile.as_view(template_name='main/profile.html'), name='profile'),
    path('info/', views.InfoView.as_view(template_name='main/info.html'), name='info')

]