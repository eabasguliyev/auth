from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns  = [
    path('',views.index,name = 'index'),
    path('register/',views.register,name = 'register'),
    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('specical_page/',views.special_page,name = 'specialPage'),
]