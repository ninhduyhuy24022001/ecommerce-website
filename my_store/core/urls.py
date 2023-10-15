from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

# namespace
app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.shop, name='shop'),
    path('about_me/', views.about_me, name='about_me'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('edit-account/', views.edit_account, name='edit_account'),
    
]
