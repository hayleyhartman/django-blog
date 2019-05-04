from django.urls import path, include
from . import views

urlpatterns = [
    path(r'^login/$', views.login_user, name='login'),
    path(r'^logout/$', views.logout_user, name='logout'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]