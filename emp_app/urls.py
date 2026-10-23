from django.urls import include, path

from std_app import admin
from . import views
urlpatterns = [
    path("",views.home),
    path("emp",views.emp),
]