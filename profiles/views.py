from django.shortcuts import render

from .models import Profile


def my_profile(request):
    obj = Profile.objects.get(user=request.user)
    ctx = {
        'obj': obj,
    }
    return render(request, 'profiles/user_profile.html', ctx)