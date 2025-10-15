from django.urls import path
from . import views

urlpatterns = [
      path('user/<int:id>/', views.user_detail, name='user_detail'),
      path('article/<int:id>/', views.article_detail, name="article"),
      path('user/<str:username>/', views.user_profile, name='user_profile'),
      path('', views.main_page, name="main_page")
#    path('form/', views.feedback_view, name='feedback'),

]

