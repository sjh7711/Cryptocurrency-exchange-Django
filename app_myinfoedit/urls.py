from django.urls import path
from app_myinfoedit import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Register your models here.


