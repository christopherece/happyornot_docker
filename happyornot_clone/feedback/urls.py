from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('results/', views.feedback_results, name='feedback_results'),
]
