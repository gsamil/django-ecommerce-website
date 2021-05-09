from django.urls import path
from .views import home, products, checkout


app_name='core'

urlpatterns = [
    path('', home, name='home')
]
