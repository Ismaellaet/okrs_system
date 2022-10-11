from django.urls import path

from .views import registration


app_name = 'core'
urlpatterns = [
    path('', registration, name='registration')
]
