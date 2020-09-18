from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('userpage', views.userpage, name='userpage'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]