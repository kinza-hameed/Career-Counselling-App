from django.urls import include , path
from .import views
from django.contrib.auth import views as auth_views
app_name ='CCA'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('test/<int:field_id>/', views.test, name='test'),
    path('result/', views.result, name='result'),
    path('english/<int:field_id>/', views.english, name='english'),
    path('register/', views.UserFromView.as_view() , name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='CCA/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='CCA/logout.html'),name='logout'),
    
]
