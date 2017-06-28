from django.shortcuts import render
from perfis.models import Profile

def index(request):
    return render(request, 'index.html')


def profile(request, profile_id):
    profile = Profile()

    if profile_id == '1':
        profile = Profile('Iury Krieger', 'iurykrieger96@gmail.com', '4989099777', 'Metasis')
    return render(request, 'profile.html', {'profile' : profile})