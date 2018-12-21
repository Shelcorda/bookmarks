from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from  django.contrib.auth.decorators import login_required

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

# login_required装饰器会检查当前用户是否通过认证
# 如果用户通过认证，则会执行装饰的视图
# 如果没有通过认证，会把用户重定向到带有一个名为next的GET参数的登录URL
# 该GET参数保存的变量为用户当前尝试访问的页面URL
@login_required
def dashboard(request):
    #section变量用来跟踪用户在站点中正在查看的页面
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

