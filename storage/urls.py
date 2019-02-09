from django.urls import path, include
from .views import *

app_name = 'storage'

urlpatterns = [
    path('', top, name='top'),
]
