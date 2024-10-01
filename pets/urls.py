from django.urls import path, include

from pets import views


urlpatterns = [
    path('add/', views.add_pets, name='add-pets'),
    path('<str:username>/pet/<slug:pet slug>', include([
        path('', views.show_pets_details, name='pets-details'),
        path('edit/', views.edit_pets, name='pets-edit'),
        path('delete/', views.delete_pets, name='pets-delete'),
    ]))
]
