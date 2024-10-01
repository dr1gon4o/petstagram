from django.shortcuts import render

# Create your views here.


def add_photos(request):
    return render(request, template_name='photo-add-page.html')


def show_photos_details(request, pk: int):
    return render(request, template_name='photo-details-page.html')


def edit_photos(request, pk: int):
    return render(request, template_name='photo-edit-page.html')
