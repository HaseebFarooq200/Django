from django.urls import path

from . import views

urlpatterns = [
    path("createuser", views.create_record, name="create_record"),
    path("getuser", views.GetUsers, name="GetUsers"),
    path('getuser/<str:userId>/', views.GetUserbyId, name='GetUserbyId'),
    path("signinuser", views.signin, name="signin"),
]