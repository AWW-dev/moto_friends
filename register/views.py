from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegisterForm, UserProfileForm

# Create your views here.
from .models import UserProfile


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

        return redirect("/")
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {"form": form, 'profile_form': profile_form})


class ShowProfileView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        return render(request, 'profil.html', {'user': user})
