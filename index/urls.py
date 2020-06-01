
from django.contrib import admin
from django.urls import include, path
from index.views import index

app_name = 'components'
urlpatterns = [
        path('', index, name='index'),
]

