from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("<int:pk>", views.CarDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
