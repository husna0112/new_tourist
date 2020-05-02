from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm, ProfileUpdateForm, UserUpdateForm



def login_view(request):


    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    context = {
        "form":form,

    }

    return render(request, "authen/form.html", context)

#loginของอาจารย์
# def my_login(request):
#     context= {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('register')
#         else:
#             error = 'Wrong username or password'
#             context['username'] = username
#             context['password'] = password
#             context['error'] = error
#     return render(request, template_name='authen/login.html', context=context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('login')

    context = {
        "form":form,
    }
    return render(request, "authen/form_regis.html", context)


#ใช้ได้
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'authen/register.html', {'form': form})





#logoutของอาจารย์
def my_logout(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,     
    }


    
    return render(request, 'authen/profile.html', context)

