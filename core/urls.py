from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path("settings", views.settings, name="settings"),
    path('logout', views.logout, name="logout"),
    path('upload', views.upload, name='upload'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('follow', views.follow, name='follow'),
    path('like-post', views.like_post, name='like-post'),
    path('search',views.search,name='search'),
    path('delete_post/<uuid:uuid>/', views.delete_post, name='delete_post'),
    path('videos',views.videos,name='videos'),
    path('uploads',views.uploads,name='uploads'),
    path('searchFighter',views.searchFighter,name='searchFighter'),


]