
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from pessoas.api import viewsets as pessoasviewsets

route = routers.DefaultRouter()
route.register(r'pessoas', pessoasviewsets.PessoasViewSet, basename="Pessoas")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] 
