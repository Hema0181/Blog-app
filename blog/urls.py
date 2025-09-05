from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('create/', views.create_post, name="create_post"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/<int:pk>/edit/', views.edit_post, name="edit_post"),
    path('post/<int:pk>/delete/', views.delete_post, name="delete_post"),
    path('profile/', views.profile_view, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
]
