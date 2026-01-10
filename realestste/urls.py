"""
URL configuration for realestste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts.views import   login_view,logout_view,analytics,dashboard_view,change_superuser_image,base,toggle_user_status
from accounts.views import delete_user,agent_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('analytics/',analytics,name='analytics'),
    path('superuser/change-image/', change_superuser_image, name="change_superuser_image"),
    path('base/',base,name='base'),
    path("user/status/<int:user_id>/", toggle_user_status, name="toggle-user"),
    path("user/delete/<int:user_id>/", delete_user, name="delete-user"),
    path('agents/agent_dashboard/',agent_dashboard,name='agents/agent_dashboard')
    
    
    
    
    
    
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)