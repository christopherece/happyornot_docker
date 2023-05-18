from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),
    path('speaker-training-dropdown/', views.speaker_training_dropdown, name='speaker_training_dropdown'),
    path('get-training-titles/', views.get_training_titles, name='get_training_titles'),
    path('save-feedback/', views.save_feedback, name='save_feedback'),
    path('results/', views.feedback_results, name='feedback_results'),
]
