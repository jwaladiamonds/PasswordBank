from django.urls import path
from dashboard import views

app_name = 'dash'
urlpatterns = [
    path('', views.home, name='home'),
]