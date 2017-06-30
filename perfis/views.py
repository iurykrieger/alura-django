from django.shortcuts import render
from perfis.models import Profile

def index(request):
    return render(request, 'index.html')


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'profile' : profile})