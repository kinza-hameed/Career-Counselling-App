from django.contrib import admin
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CCA/',include('CCA.urls')),
path('login/',auth_views.LoginView.as_view(template_name='CCA/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='CCA/logout.html'),name='logout'),
    ]
