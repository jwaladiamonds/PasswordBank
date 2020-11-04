from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('delete/<username>', views.user_delete, name='delete'),
]