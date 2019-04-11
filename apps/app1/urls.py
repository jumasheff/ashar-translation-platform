from django.urls import path
from apps.app1.views import index


urlpatterns = [
    path('', index, name='index')

]