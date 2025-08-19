"""
URL configuration for Gestion_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
    path('etudiant/', include('app_gestion.urls')),
    
]

"TASKE 1: CREATE ROUTE ETUDIANT"
"1- INSTALL drf and import it from routers url.py project"
"2- Add also router = routers.DefaultRouter(); urlpatterns = router.urls; in url.py file"
"3- Before start Serializer create Module etudiant"
"4- Now create Serializer.py file in app_gestion app and import serializer from rest_framework"
"5- Link Serializer to your Module etudiant "
"6- Now let create view.py and link it to serializer Etudiant"
"7- Go to admin.py in your app and register the new module to the built in admin page"
"8- And migrate all in db"
"Now we can call API"

"PHASE 2 TEST.PY"