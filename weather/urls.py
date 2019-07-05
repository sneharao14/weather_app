from django.conf.urls import include, url
from weather.views import *
urlpatterns = [
    # Main pages dispatcher
    url(r'^$', index, name="index"),
    url(r'delete/<city_name>/$',delete_city,name='delete_city'),
    ]	