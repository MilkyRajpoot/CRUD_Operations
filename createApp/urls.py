from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url

from .views import (
    create_view,
    detail_view,
    delete_view,
    list_view,
    update_view
    )

urlpatterns = [
    url(r'^list/$', list_view, name='list'),
    url(r'^recipe(?P<id>\d+)/$', detail_view, name='detail'),
    url(r'^create/$', create_view, name='create'),
    url(r'^recipe(?P<id>\d+)/edit/$', update_view, name='update'),
    url(r'^recipe(?P<id>\d+)/delete/$', delete_view, name='delete'),
    # path('recipe/', csrf_exempt(views.RecipeView.as_view()), name='Recipe'),
    # url(r'^api/$', csrf_exempt(views.RecipeView.as_view()), name='api'),
]