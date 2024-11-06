from django.shortcuts import render

# Create your views here.


def add_photos(request):
    return render(request, template_name='photos/photo-add-page.html')


def show_photos_details(request, pk: int):
    return render(request, template_name='photos/photo-details-page.html')


def edit_photos(request, pk: int):
    return render(request, template_name='photos/photo-edit-page.html')
