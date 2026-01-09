from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# =========================
# REDIRECT BASED ON USER
# =========================
def redirect_user(user):
    if user.is_superuser:
        return redirect('dashboard')
    else:
        return redirect('analytics')


# =========================
# LOGIN VIEW (NO login_required)
# =========================
def login_view(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect_user(user)
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login.html')


# =========================
# DASHBOARDS
# =========================
@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required
def user_dashboard(request):
    return render(request, 'pages/analytics.html')


# =========================
# LOGOUT
# =========================
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def change_superuser_image(request):
    if not request.user.is_superuser:
        return redirect("dashboard")
    if request.method == "POST" and request.FILES.get("profile_image"):
        user = request.user
        if user.profile_image:
            old_path = user.profile_image.path
            if os.path.exists(old_path):
                os.remove(old_path)       
        user.profile_image = request.FILES["profile_image"]
        user.save()
    return redirect("dashboard")








# ====================================================================================================
@login_required
def dashboard_view(request):
    return render(request,'admin/dashboard.html')

@login_required
def analytics(request):
    return render(request,'pages/analytics.html',{'page_title':'Analytics'})



def base(request):
    return render(request,'base.html')