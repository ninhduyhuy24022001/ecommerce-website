from django.urls import path

from . import views

# namespace
app_name = 'product'

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail'),
]   
