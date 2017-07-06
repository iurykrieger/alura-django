from django.shortcuts import render, redirect
from perfis.models import Profile, Invitation


def index(request):
    return render(request, 'index.html', {'profiles': Profile.objects.all(),
                                          'logged_profile': get_logged_profile(request)})


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    logged_profile = get_logged_profile(request)
    is_contact = profile in logged_profile.contacts.all()
    return render(request, 'profile.html', {'profile': profile,
                                            'logged_profile': logged_profile,
                                            'is_contact': is_contact})


def invite(request, invited_profile):
    profile = Profile.objects.get(id=invited_profile)
    logged_profile = get_logged_profile(request)
    logged_profile.invite(profile)
    return redirect('index')


def accept(request, invitation_id):
    invitation = Invitation.objects.get(id=invitation_id)
    invitation.accept()
    return redirect('index')


def get_logged_profile(request):
    return Profile.objects.get(id=1)
