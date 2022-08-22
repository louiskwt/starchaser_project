from django.shortcuts import render
from .models import SiteContent


# Create your views here.
def about_view(request):
    about_content = SiteContent.objects.get(name="about").content
    context = {
        "content": about_content
    }
    return render(request, 'about/about.html', context)

def services_view(request):
    return render(request, 'services/services.html')



def error_404_view(request, exception):
    context = {}
    return render(request, '404.html', context)

def error_500_view(request):
    context = {}
    return render(request, '500.html', context)

