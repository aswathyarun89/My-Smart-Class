from django.urls import path
from . import views
urlpatterns = [
    path('pgm',views.myfunction,name="pgm"),
]