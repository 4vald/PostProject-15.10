from django.urls import path
from . import views

urlpatterns = [
   path('form/', views.feedback_view, name='feedback'),
]