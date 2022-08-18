from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'about/about.html')

def services_view(request):
    return render(request, 'services/services.html')

