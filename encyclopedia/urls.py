from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:contentname>",views.content, name="content"),
    path("wiki/<str:contentname>",views.content, name="link"),
    path("add/", views.add, name="add"),
    path("add/<str:contentname>", views.content, name="links"),
    path("create/", views.create, name="create"),
    path("rand/", views.rand, name="rand"),
   
]
