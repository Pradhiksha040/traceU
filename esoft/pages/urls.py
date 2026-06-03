from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.root_page_view, name="home"),
    path("<str:slug>/", views.dynamic_pages, name="dynamic_pages"),
]