from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:name>/', views.hello_name),
    path('times/<int:userNum>/', views.times2),
    path('sum/<int:userNum>/', views.sum)

]