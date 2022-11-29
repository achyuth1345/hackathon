from django.urls import path
from . import views
from .views import ApiViews

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', ApiViews.as_view())
]