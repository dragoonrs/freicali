from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'juroComposto'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:igpm_id>/', views.detail, name='detail'),
    path('updateIgpm/<int:igpm_id>/', views.detail, name='updateIgpm'),

]