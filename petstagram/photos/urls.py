from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photos, name='add-photos'),
    path('<int:pk>/', include([
        path('', views.show_photos_details, name='photos-details'),
        path('edit/', views.edit_photos, name='photos-edit'),
    ]))
]
