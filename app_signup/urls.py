from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.signup, name='signup'),
    path('forgot-passwd/', views.forgot, name='forgot'),
]