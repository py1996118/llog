from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

LoginView.template_name = 'users/login.html'

app_name = 'users'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register',views.register,name='register')
]