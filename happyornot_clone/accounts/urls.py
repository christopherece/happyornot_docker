from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('feedback_form')), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('feedback_count/', views.feedback_count, name='feedback_count'),
    path('excellent-feedback/', views.excellent_feedback, name='excellent_feedback'),
    path('good-feedback/', views.good_feedback, name='good_feedback'),
    path('average-feedback/', views.average_feedback, name='average_feedback'),
    path('poor-feedback/', views.poor_feedback, name='poor_feedback'),
    path('bad-feedback/', views.bad_feedback, name='bad_feedback'),
]
