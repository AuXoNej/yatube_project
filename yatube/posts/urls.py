from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('group/<slug:slug>/', views.group_posts, name='groups')
] 