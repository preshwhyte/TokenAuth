from django.urls import path
from . import views

urlpatterns=[
    path('', views.home_list, name='home_list' ),
    path('getdetail/<str:pk>/', views.getDetail),
    path('post/',views.post, name='post'),
    path('login/', views.CustomAuthToken.as_view())

]