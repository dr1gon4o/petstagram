from django.urls import path, include

from common import views


urlpatterns = [
    path('', views.home, name='home'),
]
