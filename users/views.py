from django.shortcuts import render, redirect
from django.views.generic.base import View
from users.forms import UserForm
from django.contrib.auth.models import User
from profiles.models import Profile


class UserView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = UserForm(request.POST)
        if(form.is_valid()):

            user = User.objects.create_user(
                username=form.data['name'], email=form.data['email'], password=form.data['password'])

            profile = Profile(name=form.data['name'], phone=form.data['phone'], name_company=form.data['name_company'], user=user)
            profile.save()
            return redirect('index')

        return render(request, 'register.html', {'form': form})
