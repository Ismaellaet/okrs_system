from django.urls import path

from .views import IndexView, register


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', register, name='register')
]
