from django.shortcuts import render, redirect
from perfis.models import Profile


def index(request):
    return render(request, 'index.html', {'profiles': Profile.objects.all(),
                                          'logged_profile': get_logged_profile(request)})


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'profile': profile})


def invite(request, invited_profile):
    profile = Profile.objects.get(id=invited_profile)
    logged_profile = get_logged_profile(request)
    logged_profile.invite(profile)
    return redirect('index')


def get_logged_profile(request):
    return Profile.objects.get(id=1)
