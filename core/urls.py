from django.urls import path

from .views import register


app_name = 'core'
urlpatterns = [
    path('', register, name='register')
]
