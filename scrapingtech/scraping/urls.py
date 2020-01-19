from django.urls import path
from scraping import views

urlpatterns = [
    path("index/", views.HomePageView, name="index"),
    path("", views.HomePageView)
]
