"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('myinfo/', include('app_myinfo.urls')),
<<<<<<< HEAD
    path('holdings/', include('app_holding.urls')),
    path('account/', include('app_account.urls')),
    path('tradelog/', include('app_tradelog.urls')),
    path('signup/', include('app_signup.urls')),
    path('myinfoedit/', include('app_myinfoedit.urls')),
    
=======
    #path('trade/', include('trade.urls')),
    #path('signup/', include('signup.urls')),
    path('holdings/', include('app_holdings.urls')),
    path('tradelog/', include('app_tradelog.urls')),
    path('account/', include('app_account.urls')),
>>>>>>> 2ea214c40537f790e5f85d441917e0b3f658310a
]

