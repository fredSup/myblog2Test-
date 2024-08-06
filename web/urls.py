from django.urls import path
from .import views 
from web.views import BlogHome, BlogPostDetail, BlogPostCreate, BlogPostUpdated, BlogPostDelete
from django.contrib.auth.views import LoginView

app_name = "web"

urlpatterns = [
    path('', BlogHome.as_view(), name = 'home'),
    path('create/', BlogPostCreate.as_view(), name = 'create'),
    path('<str:slug>', BlogPostDetail.as_view(), name = 'post'),
    path('edit/<str:slug>/', BlogPostUpdated.as_view(), name = 'edit'),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name = 'delete'),


  


    #path('<str:slug>', BlogPostDetail.as_view(), name = 'post'),


    
]