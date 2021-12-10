from . import views
from django.urls import path

urlpatterns = [
    path('addition/', views.addition, name="addition"),
    path('addition/get_addition_score/',
         views.get_addition_score, name="get_addition_score"),
    path('addition/highscores/', views.high_score, name="high_score"),

    path('advanced_addition/', views.advanced_addition, name="advanced_addition"),
]
