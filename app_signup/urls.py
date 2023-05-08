from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
]