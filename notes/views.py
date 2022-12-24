from django.shortcuts import render


# Create your views here.
def notes_index_view(request):
    return render(request, 'notes_pages/notes_catalogue.html')