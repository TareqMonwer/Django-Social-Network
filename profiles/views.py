from django.shortcuts import render

from .models import Profile
from .forms import ProfileForm


def my_profile(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=obj
    )
    ctx = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'profiles/user_profile.html', ctx)