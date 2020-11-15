from django.shortcuts import render


def home_view(request):
    ctx = {
        'greet': f'Hello {request.user}'
    }
    return render(request, 'main/home.html', ctx)