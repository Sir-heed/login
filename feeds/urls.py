
from django.urls import path

from .views import feeds

app_name = "feeds"
urlpatterns = [
    path('', feeds, name="feeds"),
]