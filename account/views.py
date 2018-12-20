from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['用户名'],
                                password=cd['密码'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('成功认证')
                else:
                    return HttpResponse('帐号被禁用')
            else:
                return HttpResponse('帐号无效')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})