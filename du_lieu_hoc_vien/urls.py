from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', data_entry_main_page, name='data_entry_main'),
    url(r'^save$', entry_save, name='data_entry_save')
]
