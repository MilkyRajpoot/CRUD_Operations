from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url

urlpatterns = [
    path('index', views.index, name="index"),
    url(r'^api/$', views.InfoView.as_view(), name='api'),
]