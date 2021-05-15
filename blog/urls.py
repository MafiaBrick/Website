from django.urls import path,include
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.blog_view,name = 'blog_page'),
    path('<int:blog_id>/',views.blog_detail, name = 'detail'),
]
