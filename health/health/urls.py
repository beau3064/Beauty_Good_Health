"""health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
 
from health_app import views
 
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from social_core.utils import setting_name
from health_app.feeds import LatestPostsFeed, AtomSiteNewsFeed
from django.contrib.auth import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('lifestyle', views.lifestyle, name="lifestyle"),
    path('food', views.food, name="food"),
    path('health', views.health, name="health"),
    path('beauty', views.beauty, name="beauty"),
    path('video', views.video, name="video"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('search/', views.board_search, name="board_search"),
    path("create_post/", views.create_post, name="create_post"),
    path('oauth/', include('social_django.urls', namespace='social')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    #path('login/', include("django.contrib.auth.urls")),
    path('login/', views.login, name='login'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("summernote/", include("django_summernote.urls")),
    path("post_page/", views.PostList.as_view(), name="post_page"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
