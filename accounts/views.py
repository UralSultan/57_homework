from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST


def login_view(request):
    context = {'username': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username or ''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects_view')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


@require_POST
def logout_view(request):
    logout(request)
    return redirect('projects_view')
