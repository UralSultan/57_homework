from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from .forms import MyUserCreateForm


def redirect_after_auth(request, next_url=None):
    next_url = next_url or request.POST.get('next') or request.GET.get('next')

    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)

    return redirect('projects_view')


def login_view(request):
    next_url = request.POST.get('next') or request.GET.get('next', '')
    context = {'username': '', 'next': next_url}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username or ''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_after_auth(request, next_url)
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


@require_POST
def logout_view(request):
    next_url = request.POST.get('next') or request.GET.get('next')
    logout(request)
    return redirect_after_auth(request, next_url)


def register_view(request, *args, **kwargs):
    next_url = request.POST.get('next') or request.GET.get('next', '')
    if request.method == 'POST':
        form = MyUserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_after_auth(request, next_url)
    else:
        form = MyUserCreateForm()
    return render(request, 'user_create.html', context={'form': form, 'next': next_url})
