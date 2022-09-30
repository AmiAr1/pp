from django.urls import path
from .views import list_view, detail_view


app_name ="dorama"

urlpatterns = [
    path("", list_view, name="list"),
    path("<int:pk>", detail_view, name="detail"),
]
