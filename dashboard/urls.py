
from django.urls import path

from .views import (home, verified, index, logout_view, 
post_detail_edit)

app_name = "dashboard"
urlpatterns = [
    path('', home, name="home"),
    path('verified/', verified, name="verified"),
    path('index/', index, name="index"),
    path('logout/', logout_view, name="logout"),
    path('edit/<slug:post>/', post_detail_edit, name="edit"),
]