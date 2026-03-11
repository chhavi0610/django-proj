"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blog.views import home, about, contact, create_post, signup, user_login, user_logout, edit_post, delete_post, profile
from blog import apiviews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('contact/',contact),
    path('', home),
    path('signup/', signup),
    path('login/', user_login),
    path('logout/', user_logout),
    path('create/', create_post),
    path("/edit/<int:post_id>/",  edit_post, name='edit_post'),
    path("/delete/<int:post_id>/", delete_post, name='delete_post'),
    path("posts/", apiviews.get_posts),
    path("posts/<int:id>", apiviews.get_post, name="get_post"),
    path("posts/create", apiviews.create_post),
    path("posts/delete/<int:id>", apiviews.delete_post),
    path('api/token' , TokenObtainPairView.as_view(), name="token_obtain_view"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="token_refresh_view"),
    path("profile/",profile, name="profile"),
]
