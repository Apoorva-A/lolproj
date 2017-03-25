from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # define the url getdata that we have written inside form
    # url(r'^summoner_one/', views.index),
    url(r'summoner_one', views.summoner_one, name="summoner_one"),


    # defining the view for root URL
    url(r'^$', views.index),
]
