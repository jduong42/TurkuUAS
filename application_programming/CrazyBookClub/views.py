from django.shortcuts import render

# Create your views here.

def index(request):
    # The home page for CrazyBookClub
    return render(request, 'CrazyBookClub')