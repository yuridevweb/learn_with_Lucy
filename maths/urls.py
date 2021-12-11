from . import views
from django.urls import path

urlpatterns = [
    path('maths/', views.maths, name="maths"),
    path('addition/', views.addition, name="addition"),
    path('addition/get_addition_score/',
         views.get_addition_score, name="get_addition_score"),
    path('addition/highscores/', views.high_score, name="high_score"),

    path('advanced_addition/', views.advanced_addition, name="advanced_addition"),
    path('addition/get_advanced_add_score/',
         views.get_advanced_add_score, name="get_advanced_add_score"),

    path('simple_addition/', views.simple_addition, name="simple_addition"),
    path('addition/get_simple_add_score/',
         views.get_simple_add_score, name="get_simple_add_score"),
]
