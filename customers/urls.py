from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_customer, name="add_customer"),
    path("delete/<int:pk>/", views.delete_customer, name="delete_customer"),
]
