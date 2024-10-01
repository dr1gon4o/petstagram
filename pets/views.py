from django.shortcuts import render

# Create your views here.


def add_pets(request):
    return render(request, template_name='pet-add-page.html')


# def pets(request):
#     return render(request, template_name='login-page.html')


def show_pets_details(request, username: str, pet_slug: str):
    return render(request, template_name='pet-details-page.html')


def edit_pets(request, username: str, pet_slug: str):
    return render(request, template_name='pet-edit-page.html')


def delete_pets(request, username: str, pet_slug: str):
    return render(request, template_name='pet-delete-page.html')
