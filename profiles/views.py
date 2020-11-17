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
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    ctx = {
        'obj': obj,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/user_profile.html', ctx)
